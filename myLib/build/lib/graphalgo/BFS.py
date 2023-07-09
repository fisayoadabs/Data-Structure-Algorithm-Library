from pathlib import Path

import sys
path_root = Path(__file__).parents[4]
sys.path.append(str(path_root))

from collections import deque

class BFS:
    def __init__(self, graph):
        self.graph = graph
    
    def traverse(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            v = queue.popleft()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor, weight in self.graph.adj_list[v]:
                    if neighbor not in visited:
                        queue.append(neighbor)