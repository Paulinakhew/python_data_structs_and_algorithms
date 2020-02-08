import pytest
import breadth_first_search_traversal as bfst


def test_bfst_order():
    # sample search space, represented by a dictionary
    graph = {
        'A': ['B', 'C', 'E'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B', 'E'],
        'E': ['A', 'B', 'D'],
        'F': ['C'],
        'G': ['C']
    }

    explored = bfst.bfs_connected_component(graph, 'A')
    assert explored == ['A', 'B', 'C', 'E', 'D', 'F', 'G']


def test_shortest_path():
    # sample search space, represented by a dictionary
    graph = {
        'A': ['B', 'C', 'E'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B', 'E'],
        'E': ['A', 'B', 'D'],
        'F': ['C'],
        'G': ['C']
    }

    shortest_path = bfst.bfs_shortest_path(graph, 'G', 'D')
    assert shortest_path == ['G', 'C', 'A', 'B', 'D']
