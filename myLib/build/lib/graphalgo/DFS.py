from pathlib import Path

import sys
path_root = Path(__file__).parents[4]
sys.path.append(str(path_root))


class DFS:
    def __init__(self, graph):
        self.graph = graph
    
    def traverse(self, start):
        visited = set()
        stack = [start]
        while stack:
            v = stack.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor, weight in self.graph.adj_list[v]:
                    if neighbor not in visited:
                        stack.append(neighbor)
