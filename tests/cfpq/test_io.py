import os
from networkx import MultiDiGraph
from project.cfpq.io import save_graph_as_dot_file, load_graph_by_name


def test_load_graph_by_name_bzip():
    actual_graph = load_graph_by_name("bzip")

    assert 632 == actual_graph.number_of_nodes()
    assert 556 == actual_graph.number_of_edges()


def test_save_graph_as_dot_file():
    graph = MultiDiGraph()
    for i in [1, 2, 3]:
        graph.add_node(i)
    graph.add_edge(1, 3, label="a")
    graph.add_edge(2, 3, label="b")

    curr_dir_path = os.path.dirname(os.path.realpath(__file__))
    expected_file_path = os.path.join(curr_dir_path, "test_io_expected_graph.dot")
    actual_file_path = os.path.join(curr_dir_path, "test_io_actual_graph.dot")

    assert save_graph_as_dot_file(graph, actual_file_path)

    with open(expected_file_path, "r") as expected_file:
        with open(actual_file_path, "r") as actual_file:
            assert expected_file.read() == actual_file.read()
