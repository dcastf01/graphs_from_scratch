import json
import os

import matplotlib.pyplot as plt


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

    def number_in_degrees(self):
        # for
        adj_out_lit = {v: [] for v in self.vertices}

        for s, t in self.edges:
            adj_out_lit[str(t)].append(s)

        degrees = {}
        for k, v in self.adjlist.items():

            degrees[len(v)] = degrees[len(v)] + 1 if len(v) in degrees else 1
        return degrees

    def number_out_degrees(self):
        degrees = {}
        for k, v in self.adjlist.items():

            degrees[len(v)] = degrees[len(v)] + 1 if len(v) in degrees else 1
            #  +=1
            # else:
            # degrees[len(v)] =1
        return degrees

    def plot_histogram(self, filename):
        '''Functionality to plot a histogram of vertex in- and out-degrees and save it as
        PNG with appropriate title and axes labelling.'''
        degrees_in = self.number_in_degrees()
        degrees_out = self.number_out_degrees()

        fig, ax = plt.figure("Degree of our graph", figsize=(16, 8))
        print('asdad')

        pass


a = Graph.deserialize_to_json('/home/graphs_from_scratch/workspace/test/data_test/test.json')
a.plot_histogram()
