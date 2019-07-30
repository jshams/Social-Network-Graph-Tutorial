#!python


class Vertex(object):
    """ Vertex Class
    A helper class for the Graph class that defines vertices and vertex
    neighbors.
    """

    def __init__(self, vertex_id: str):
        self.id = vertex_id
        self.neighbors = dict()

    def add_neighbor(self, neighbor_key, weight=1):
        '''Adds a edge from this vertex to the given neighboring vertex with the given weight'''
        self.neighbors[neighbor_key] = weight

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return f"{self.id} adjacent to {[neighbor for neighbor in self.neighbors]}"

    def is_neighbors_with(self, key: str):
        '''Returns a boolean indicating whether the vertex is pointing to another item'''
        return key in self.neighbors

    def __hash__(self):
        return hash(self.id)

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return [neighbor for neighbor in self.neighbors]

    def get_id(self):
        """Return the id of this vertex."""
        return self.id

    def get_edge_weight(self, vertex_key: str):
        """Return the weight of this edge."""
        return self.neighbors[vertex_key]
