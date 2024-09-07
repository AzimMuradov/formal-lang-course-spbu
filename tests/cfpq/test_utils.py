import pytest
from networkx import MultiDiGraph
from project.cfpq.utils import create_labeled_two_cycles_graph


def test_create_labeled_two_cycles_graph():
    expected_graph = MultiDiGraph(
        [
            (0, 1, {"label": "a"}),
            (1, 2, {"label": "a"}),
            (2, 3, {"label": "a"}),
            (3, 0, {"label": "a"}),
            (0, 4, {"label": "b"}),
            (4, 5, {"label": "b"}),
            (5, 6, {"label": "b"}),
            (6, 7, {"label": "b"}),
            (7, 0, {"label": "b"}),
        ]
    )
    actual_graph = create_labeled_two_cycles_graph((3, "a"), (4, "b"))

    assert expected_graph.nodes == actual_graph.nodes
    assert set(expected_graph.edges.data(data="label")) == set(
        actual_graph.edges.data(data="label")
    )


def test_create_labeled_two_cycles_graph_not_positive_number_of_nodes():
    with pytest.raises(ValueError):
        create_labeled_two_cycles_graph((0, "a"), (4, "b"))
    with pytest.raises(ValueError):
        create_labeled_two_cycles_graph((2, "a"), (0, "b"))
    with pytest.raises(ValueError):
        create_labeled_two_cycles_graph((0, "a"), (0, "b"))
    with pytest.raises(ValueError):
        create_labeled_two_cycles_graph((-1, "a"), (4, "b"))
    with pytest.raises(ValueError):
        create_labeled_two_cycles_graph((1, "a"), (-2, "b"))
    with pytest.raises(ValueError):
        create_labeled_two_cycles_graph((-1, "a"), (-4, "b"))
