from pathlib import Path
import sys
path_root = Path(__file__).parents[4]
sys.path.append(str(path_root))

from myLib.build.lib.graphalgo.BFS import BFS
from myLib.build.lib.graphalgo.DFS import DFS
from myLib.build.lib.graphalgo.Graph import Graph


g = Graph()
g.add_edge('A', 'B', 2)
g.add_edge('A', 'C', 1)
g.add_edge('B', 'C', 3)
g.add_edge('C', 'D', 4)


print("\n-------------------------TESTING BFS-------------------------")
bfs = BFS(g)
bfs.traverse('A')



print("\n-------------------------TESTING DFS-------------------------")
dfs = DFS(g)
dfs.traverse('A')


print("------------------------------END----------------------------")