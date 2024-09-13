from networkx import Graph, MultiDiGraph
from project.cfpq.graph_info import GraphInfo, get_graph_info


def test_get_graph_info_empty_graph():
    graph = Graph()

    expected_graph_info = GraphInfo()
    actual_graph_info = get_graph_info(graph)

    assert expected_graph_info == actual_graph_info


def test_get_graph_info_nonempty_graph():
    graph = MultiDiGraph()
    for i in [1, 2, 3, 4, 5]:
        graph.add_node(i)
    graph.add_edge(1, 3, label="a")
    graph.add_edge(2, 3, label="b")
    graph.add_edge(4, 1, label="a")
    graph.add_edge(1, 4, label="c")

    expected_graph_info = GraphInfo(
        number_of_nodes=5, number_of_edges=4, unique_labels={"a", "b", "c"}
    )
    actual_graph_info = get_graph_info(graph)

    assert expected_graph_info == actual_graph_info
