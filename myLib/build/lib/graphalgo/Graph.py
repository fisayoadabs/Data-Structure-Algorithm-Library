class Graph:
    def __init__(self):
        self.order = 0
        self.size = 0
        self.adj_list = {}
    
    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []
            self.order += 1
    
    def add_edge(self, u, v, weight=None):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].append((v, weight))
        self.size += 1
