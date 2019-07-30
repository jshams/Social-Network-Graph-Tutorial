from vertex import Vertex
from file_reader import FileReader
from queue import Queue


class Graph(object):
    def __init__(self, FILE_PATH=None):
        """Initialize a graph object after reading from a file if one is provided"""
        self.f = FileReader(FILE_PATH)
        self.vertices = {}  # dictionary of verticies
        self.edges = []
        self.vertex_count = 0
        self.edge_count = 0
        self.digraph = None
        if FILE_PATH is not None:
            all_verticies = self.f.verticies
            self.add_verticies(all_verticies)
            self.edges = self.f.edges
            self.digraph = self.f.digraph
            self.add_egdes(self.edges)

    def __iter__(self):
        '''yields each vertex key'''
        for vertex in self.vertices:
            yield vertex

    def add_vertex(self, vert):
        '''adds an instance of Vertex to the graph.'''
        self.vertices[vert] = Vertex(vert)
        self.vertex_count += 1

    def add_verticies(self, verts):
        for vert in verts:
            self.add_vertex(vert)

    def get_vertex(self, vert_key):
        '''finds the vertex in the graph named vertKey. Or returns None if not found'''
        if vert_key in self.vertices:
            return self.vertices[vert_key]

    def add_edge(self, from_key, to_key, weight=1):
        '''Adds a new, weighted, directed edge to the graph that connects two vertices.'''
        if from_key not in self.vertices:
            raise KeyError(f'{from_key} vertex not found in graph')
        if to_key not in self.vertices:
            raise KeyError(f'{to_key} vertex not found in graph')
        self.get_vertex(from_key).add_neighbor(to_key, weight)
        self.edge_count += 1
        if self.digraph is False:
            self.get_vertex(to_key).add_neighbor(from_key, weight)

    def add_egdes(self, edges):
        for edge in edges:
            self.add_edge(*edge)

    def get_vertices(self):
        '''returns the list of all vertices in the graph.'''
        return [vertex for vertex in self]

    def get_neighbor_keys(self, x):
        '''lists all vertices y such that there is an edge from the vertex x to the vertex y.'''
        return list(x.neighbors.keys())

    def get_neighbors(self, x):
        '''lists all vertices y such that there is an edge from the vertex x to the vertex y.'''
        # return [neighbor for neighbor in x.neighbors.values()]
        return list(x.neighbors.values())

    def breadth_first_search(self, start: str):
        '''traverses the graph in BFS order from a start'''
        seen = {start}
        queue = Queue([start])
        print(start)
        while not queue.is_empty():
            vertex_key = queue.dequeue()
            for neighbor in self.get_vertex(vertex_key).neighbors:
                if neighbor not in seen:
                    print(neighbor)
                    seen.add(neighbor)
                    queue.enqueue(neighbor)
        return list(seen)

    def find_path(self, start: str, end: str):
        self.find_shortest_path(start, end)

    def find_shortest_path(self, start: str, end: str):
        '''finds the shortest path between two points and returns None if there are none'''
        seen = {start: [start]}
        queue = Queue([start])
        while not queue.is_empty():
            vertex_key = queue.dequeue()
            for neighbor in self.get_vertex(vertex_key).neighbors:
                if neighbor not in seen:
                    seen[neighbor] = seen[vertex_key] + [neighbor]
                    if neighbor == end:
                        # print(seen[neighbor])
                        return seen[neighbor]
                    queue.enqueue(neighbor)
        return None

    def clique(self):
        from random import choice
        choice(self.get_vertices())
        # Start with an arbitrary vertex u and add it to the clique
        clique_list = set()
        for vertex in self.get_vertices():
            # For v in remaining vertices not in the clique
            in_clique = True
            # If v is adjacent to every other vertex already in the clique.
            for clique_vetex in clique_list:
                if not self.get_vertex(clique_vetex).is_neighbors_with(vertex):
                    in_clique = False
            if in_clique:
                clique_list.add(vertex)
                # Add v to the clique
        return clique_list


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.add_vertex("Friend 1")
    g.add_vertex("Friend 2")
    g.add_vertex("Friend 3")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.add_edge("Friend 1", "Friend 2")
    g.add_edge("Friend 2", "Friend 3")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print()
    print(f"The vertices are: \n{g.get_vertices()} \n")

    # Print edges
    print("The edges are: ")
    for v in g:
        for w in g.get_vertex(v).get_neighbors():
            print(f"({v}, {w})")
    print()
