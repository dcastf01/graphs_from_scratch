


class Graph():

    def __init__(self) -> None:
        '''A Python class that represents a directed graph. Graphs are constructed from
        a list of vertices and a list of edges, where each edge is a tuple like
        (source_vertex, target_vertex).
        '''
        pass

    def number_edges(self):
        pass
    def number_vertices(self):
        pass
    def number_edges_and_vertices(self):
        '''Methods to compute the number of edges and vertices.'''
        edges=self.number_edges()
        vertices=self.number_vertices()
        return edges+vertices
    def serialize_to_json(self):
        '''Methods to serialize and deserialize the graph in JSON.'''
        pass
    def deserialize_to_json(self):
        '''Methods to serialize and deserialize the graph in JSON.'''
        pass

    def plot_histogram(self):
        '''Functionality to plot a histogram of vertex in- and out-degrees and save it as
        PNG with appropriate title and axes labelling.'''