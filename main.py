
import networkx as nx
import  sys
import matplotlib.pyplot as plt
import pyttsx3
import speech_recognition as sr
import pyaudio


G=nx.Graph()
G.add_weighted_edges_from([('Skopje', 'Petrovets', 20), ('Skopje', 'Tetovo', 52), ('Petrovets', 'Kumanovo', 30),
                               ('Kumanovo', 'Kriva_planka', 63), ('Kumanovo', 'Sveti_nicole', 41),
                               ('Sveti_nicole', 'Shtip', 28),
                               ('Kochani', 'Shtip', 40), ('Kochani', 'Delchevo', 53), ('Shtip', 'Radovish', 40),
                               ('Radovish', 'Strumitsa', 31), ('Strumitsa', 'Novo_solo', 22),
                               ('Strumitsa', 'Valandovo', 23),
                               ('Valandovo', 'smokirtsa', 12), ('smokirtsa', 'Gevgelija', 17),
                               ('smokirtsa', 'Demir_kapija', 31),
                               ('Demir_kapija', 'Negotino', 21), ('smokirtsa', 'Gevgelija', 17),
                               ('Negotino', 'Gradsko', 20),
                               ('Petrovets', 'Veles', 35), ('Veles', 'Gradsko', 31), ('Gradsko', 'Prilep', 54),
                               ('Veles', 'chashka', 23),
                               ('chashka', 'Prilep', 68), ('Tetovo', 'Gostivar', 28), ('Gostivar', 'Zajas', 37),
                               ('Zajas', 'Kichevo', 11),
                               ('Kichevo', 'Prilep', 70), ('Gostivar', 'Debar', 68), ('Kichevo', 'Vraneshtitsa', 11),
                               ('Zajas', 'Kichevo', 11),
                               ('Kichevo', 'Prilep', 70), ('Gostivar', 'Debar', 68), ('Kichevo', 'Vraneshtitsa', 11),
                               ('Valandovo', 'Dojra', 24),
                               ('Veles', 'Gradsko', 31), ('Debar', 'Struga', 52), ('Debar', 'Izvor', 42),
                               ('Izvor', 'Kichevo', 14),
                               ('Izvor', 'Podmolyé', 42), ('Podmolyé', 'Ohrid', 15), ('Ohrid', 'Resen', 37),
                               ('Resen', 'Bitola', 34),
                               ('Struga', 'Podmolyé', 9), ('Gostivar', 'Zajas', 37), ('Bitola', 'Prilep', 43),
                               ('Vraneshtitsa', 'Demir_hisar', 60),
                               ('Demir_hisar', 'Bitola', 28)])


#
###############################################################################################################



try:
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', 'french')


        def speak(audio):
            engine.say(audio)
            engine.runAndWait()


        def VoiceCommand():
            r = sr.Recognizer()
            with sr.Microphone() as source:

                print("Recognizing...")
                r.pause_threshold = 1
                audio = r.listen(source)
            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='Francais')
                print(f"User said: {query}\n")
            except Exception as e:
                print(e)
                print("Unable to Recognize your voice.")
                return "None"
            return query
###############################################################################################################
        while True:
            work = VoiceCommand().lower()
            if 'bonjour' in work:
                speak('bonjour Monsieur je suis un assistant vocale pour aider dans cette application')

                print("1_ Visualisation du Graphe")
                speak("taper 1 pour visualiser le graphe")
                print("2_ L'Alghorithme de Dijkstra")
                speak("taper 2 pour le plus court chemin avec l'algorithme de dijekstra")
                print("3_ Méthode du Profondeur")
                speak("taper 3 pour l'algorithme de parcours en profondeur")
                print("4_ Méthode du Largeur")
                speak("taper 4 pour l'algorithme de parcours en largeur'")
                print("5_ L'Algorithme de Bellman_Ford")
                speak("taper 5 pour le plus court chemin avec l'algorithme de bellman_ford")
                print("6_ L'Algorithme De Floyd_Warshall")
                speak("taper 6 pour le plus court chemin avec l'algorithme de floyd_warshall")
                print("7_ Quitter")
                speak("7_taper 7 pour quitter")
                choix = int(input())


                if choix == 1:
                    nx.draw(G, with_labels=True)
                    plt.show()

                elif choix == 2:
                    source = str(input("dooner moi le source"))
                    destination = str(input("dooner moi le destination"))
                    nlength = nx.dijkstra_path_length(G, source, destination)
                    nlength2 = nx.dijkstra_path(G, source, destination)
                    print(f"La distance entre {source} et {destination} est {nlength}")
                    speak(f"La distance entre {source} et {destination} est {nlength}")
                    print(f"La distance entre {source} et {destination} est {nlength2}")
                    speak(f"La distance entre {source} et {destination} est {nlength2}")

                    pass
                elif choix == 3:
                    source = str(input("dooner moi le source"))
                    destination=str(input("dooner moi la destination"))
                    def dfs_shortest_path(graph, start, goal):
                        stack = [(start, [start])]
                        shortest_path = None

                        while stack:
                            (vertex, path) = stack.pop()

                            if vertex == goal:
                                if shortest_path is None or len(path) < len(shortest_path):
                                    shortest_path = path
                            else:
                                neighbors = list(graph.neighbors(vertex))
                                neighbors.reverse()  # Reverse the order of neighbors for DFS

                                for next_vertex in neighbors:
                                    if next_vertex not in path:
                                        stack.append((next_vertex, path + [next_vertex]))

                        return shortest_path


                    path = dfs_shortest_path(G, source,destination)
                    print(path)
                    speak( path)
                    pass
                elif choix == 4:
                    source = str(input("dooner moi le source"))
                    destination = str(input("dooner le destination"))
                    path = nx.shortest_path(G, source, destination, weight='distance')
                    print(path)
                    speak(path)
                    pass



                elif choix == 5:
                    source = str(input("dooner moi le source"))
                    destination = str(input("dooner le destination"))
                    v1=nx.bellman_ford_path(G,source,destination)
                    print(f"La direction entre {source} et {destination} est {v1}")
                    speak(f"La direction entre {source} et {destination} est {v1}")
                    v2 = nx.bellman_ford_path_length(G, source, destination)
                    print(f"La distance entre {source} et {destination} est {v2}")
                    speak(f"La distance entre {source} et {destination} est {v2}")
                elif choix == 6:
                    source = str(input("dooner moi le source"))
                    destination = str(input("dooner le destination"))


                    def floyd_warshall(G, depart, arrivee):
                        ville_to_index = {v: i for i, v in enumerate(G.nodes)}
                        nv = nx.relabel_nodes(G, ville_to_index)
                        a_index = ville_to_index[depart]
                        b_index = ville_to_index[arrivee]
                        dist = nx.floyd_warshall_numpy(nv)
                        return dist[a_index][b_index]
                    print(floyd_warshall(G,source,destination))
                    speak( floyd_warshall(G,source,destination))
                elif choix== 7:
                    sys.exit(0)


except BaseException as ex:
 print(f"error occured = {ex}")

finally:
     print("Thank you .....bye..have a nice day")