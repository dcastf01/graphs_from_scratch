import json
import os


class Graph:
    def __init__(self, vertices: list, edges: list) -> None:
        '''A Python class that represents a directed graph. Graphs are constructed from
        a list of vertices and a list of edges, where each edge is a tuple like
        (source_vertex, target_vertex).
        '''

        self.vertices = [str(v) for v in vertices]
        self.edges = edges
        # we create a dictionary with all the nodes with a empty list
        self.adjlist = {v: [] for v in self.vertices}

        for s, t in self.edges:
            self.adjlist[str(s)].append(t)
        # [ self.adjfor s,t in self.edges]

    def number_edges(self):
        return len(self.edges)

    def number_vertices(self):
        return len(self.vertices)

    def number_edges_and_vertices(self):
        '''Methods to compute the number of edges and vertices.'''
        edges = self.number_edges()
        vertices = self.number_vertices()
        return edges + vertices

    def serialize_to_json(self, json_file='sample.json'):
        '''Methods to serialize and deserialize the graph in JSON.'''

        with open(json_file, 'w') as outfile:
            json.dump(self.adjlist, outfile)

    @classmethod
    def deserialize_to_json(cls, json_file='sample.json'):
        '''Methods to serialize and deserialize the graph in JSON.'''
        with open(json_file) as f:
            js_graph = json.load(f)
        edges = []
        for s, list_values in js_graph.items():
            for v in list_values:
                edges.append((s, v))

        # edges= for
        return cls(js_graph.keys(), edges)

    def plot_histogram(self):
        '''Functionality to plot a histogram of vertex in- and out-degrees and save it as
        PNG with appropriate title and axes labelling.'''
        pass


Graph.deserialize_to_json('/home/graphs_from_scratch/workspace/test/data_test/test.json')
