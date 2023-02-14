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

        return cls(js_graph.keys(), edges)

    def number_in_degrees(self):
        adj_out_lit = {v: [] for v in self.vertices}

        for s, t in self.edges:
            adj_out_lit[str(t)].append(s)

        degrees = {}
        # here we got a error, we got the adj to calculate the out degrees
        # also the logic to calculate this value should be a function,
        # because we are repeating the same logic in the number_out_degrees
        for k, v in adj_out_lit.items():

            degrees[len(v)] = degrees[len(v)] + 1 if len(v) in degrees else 1
        return dict(sorted(degrees.items()))  # we have added sorted to ease the output

    def number_out_degrees(self):
        degrees = {}
        for k, v in self.adjlist.items():

            degrees[len(v)] = degrees[len(v)] + 1 if len(v) in degrees else 1

        return dict(sorted(degrees.items()))  # we have added sorted to ease the output

    def plot_histogram(self, filename='sample.png'):
        '''Functionality to plot a histogram of vertex in- and out-degrees and save it as
        PNG with appropriate title and axes labelling.'''
        degrees_in = self.number_in_degrees()
        deg_in, cnt_in = zip(*degrees_in.items())  # we can remove it

        degrees_out = self.number_out_degrees()
        deg_out, cnt_out = zip(*degrees_out.items())  # no can remove it

        plt.rcParams["figure.figsize"] = (18, 12)
        fig, axs = plt.subplots(2)
        fig.suptitle("Title for whole figure", fontsize=16)
        # we need to use bar instead of hist because we calculate previously the number of instances per degree (counting)
        # probably in plt.subplots(sharex=True) should be enough
        # axs[0].hist(degrees_in)
        axs[0].bar(degrees_in.keys(), degrees_in.values())
        axs[0].set_title('Degrees In')

        # axs[1].hist(algo)
        axs[1].bar(degrees_out.keys(), degrees_out.values())
        axs[1].set_title('Degrees out')
        # maybe use the same axis x to both ax
        for ax in axs.flat:
            ax.set(xlabel='degree', ylabel='counts')

        plt.savefig(filename)
        return fig, axs
