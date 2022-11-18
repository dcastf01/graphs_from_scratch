import os

import pytest

from graphs_from_scratch.graph_class import Graph

vertices = [0, 1, 2, 3, 4, 5]
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
f_path = os.path.join('data_test', 'test.json')


def test_num_edges_ad_vertices():

    g = Graph(vertices, edges)
    number_elements = g.number_edges_and_vertices()
    assert number_elements == (len(vertices) + len(edges))
    print(g.number_edges_and_vertices())


def test_serialize():
    # we check if we create a file json or not in data
    g = Graph(vertices, edges)
    os.makedirs('data_test', exist_ok=True)

    g.serialize_to_json(f_path)
    assert os.path.isfile(f_path)


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
    g = Graph.deserialize_to_json(f_path)
    int_vertices = [int(v) for v in g.vertices]
    int_edges = [(int(s), t) for s, t in g.edges]
    assert int_vertices == vertices
    assert int_edges == edges


# test_deserialize()
