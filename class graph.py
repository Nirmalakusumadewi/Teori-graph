class Graph:
    def __init__(self, gdict=None):
        self.gdict = gdict if gdict else {}

    def get_vertex(self):
        return list(self.gdict.keys())

    def get_edges(self):
        edges = []
        for v in self.gdict:
            for e in self.gdict[v]:
                edge = {v, e}  # membuat set sisi
                if edge not in edges and {e, v} not in edges:  # mengecek apakah sisi sudah ada
                    edges.append(edge)
        return edges

    def add_vertex(self, v):
        if v not in self.gdict:
            self.gdict[v] = []

    def add_edge(self, e):
        v1, v2 = e
        if v1 in self.gdict:
            if v2 not in self.gdict[v1]:
                self.gdict[v1].append(v2)
        else:
            self.gdict[v1] = [v2]
        
        if v2 in self.gdict:
            if v1 not in self.gdict[v2]:
                self.gdict[v2].append(v1)
        else:
            self.gdict[v2] = [v1]

# Example usage:
graph1 = {1: [2, 3],
          2: [1, 2],
          3: [1, 4],
          4: [5],
          5: [4]}

g = Graph(graph1)
print("Vertices awal:", g.get_vertex())
print("Edges awal:", g.get_edges())

g.add_vertex(6)
print("Vertices setelah menambah vertex 6:", g.get_vertex())

g.add_edge((1, 2))
print("Edges setelah menambah edge (1, 2):", g.get_edges())

g.add_edge((6, 1))
print("Vertices setelah menambah vertex 6 dan edge (6, 1):", g.get_vertex())
print("Edges setelah menambah edge (6, 1):", g.get_edges())
