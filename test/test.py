import os
import random

import numpy as np
import pytest

from graphs_from_scratch.graph_class import Graph

vertices = [0, 1, 2, 3, 4, 5]
vertices = list(range(0, random.randint(0, 100)))
max_value = vertices[-1]
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
edges = []
for tup in range(
    random.randint(max_value // 2, max_value * 2),  # to have at least the half number of connections than vertices
):

    edges.append((random.randint(0, max_value), random.randint(0, max_value)))

f_path_json = os.path.join('data_test', 'test.json')
f_path_image = os.path.join('data_test', 'histogram.png')


def test_num_edges_ad_vertices():

    g = Graph(vertices, edges)
    number_elements = g.number_edges_and_vertices()
    assert number_elements == (len(vertices) + len(edges))
    print(g.number_edges_and_vertices())


def test_serialize():
    # we check if we create a file json or not in data
    g = Graph(vertices, edges)
    os.makedirs('data_test', exist_ok=True)

    g.serialize_to_json(f_path_json)
    assert os.path.isfile(f_path_json)


def test_out_degree():
    # wecopy and paste in the case we modify the main user case
    vertices = [0, 1, 2, 3, 4, 5]
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
    g = Graph(vertices, edges)
    assert g.number_out_degrees()[0] == 1
    assert g.number_out_degrees()[1] == 5


def test_in_degree():
    # wecopy and paste in the case we modify the main user case
    vertices = [0, 1, 2, 3, 4, 5]
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
    g = Graph(vertices, edges)
    assert g.number_out_degrees()[0] == 1
    assert g.number_out_degrees()[1] == 5


def test_deserialize():
    test_serialize()
    # we check if we create a file json or not in data
    g = Graph.deserialize_to_json(f_path_json)
    int_vertices = [int(v) for v in g.vertices]
    int_edges = [(int(s), t) for s, t in g.edges]
    assert int_vertices == vertices
    assert len(int_edges) == len(edges)


def create_plot_and_check_if_has_title_and_axis():

    g = Graph(vertices, edges)
    fig, axs = g.plot_histogram(f_path_image)
    for ax in axs:
        assert ax.get_title() != ''
        assert ax.get_xlabel() != ''
        assert ax.get_ylabel() != ''
