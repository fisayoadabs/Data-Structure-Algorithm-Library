from pathlib import Path
import sys
path_root = Path(__file__).parents[4]
sys.path.append(str(path_root))

from myLib.build.lib.graphalgo.Dijkstra import Dijkstra, Graph




graph = Graph()
graph.add_edge('A', 'B', 2)
graph.add_edge('A', 'C', 1)
graph.add_edge('B', 'C', 5)
graph.add_edge('B', 'D', 1)
graph.add_edge('C', 'B', 3)
graph.add_edge('C', 'D', 4)
graph.add_edge('D', 'B', 7)
graph.add_edge('D', 'A', 2)

print("\n-------------------------TESTING DIJKSTRA-------------------------\n")
dijkstra = Dijkstra(graph)
distances = dijkstra.shortest_path('A')
print(distances) 

print("\n------------------------------END----------------------------")

