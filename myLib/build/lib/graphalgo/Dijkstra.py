import heapq

from pathlib import Path
import sys
path_root = Path(__file__).parents[4]
sys.path.append(str(path_root))


class Graph:
    def __init__(self):
        self.order = 0
        self.size = 0
        self.adj_list = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.order += 1
            self.adj_list[vertex] = {}
        
    def add_edge(self, source, dest, weight=1):
        if source not in self.adj_list:
            self.add_vertex(source)
        if dest not in self.adj_list:
            self.add_vertex(dest)
        self.adj_list[source][dest] = weight
        self.size += 1

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        
    def shortest_path(self, source):
        distances = {vertex: float('infinity') for vertex in self.graph.adj_list}
        distances[source] = 0
        
        priority_queue = [(0, source)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            if current_distance > distances[current_vertex]:
                continue
            
            for neighbor, weight in self.graph.adj_list[current_vertex].items():
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances
