from dataclasses import dataclass, field

from networkx import Graph


@dataclass(frozen=True)
class GraphInfo:
    """Graph info.

    Attributes
    ----------
    number_of_nodes : int
        The number of nodes in the graph.
    number_of_edges : int
        The number of edges in the graph.
    unique_labels : set[str]
        The set of labels in the graph.
    """

    number_of_nodes: int = 0
    number_of_edges: int = 0
    unique_labels: set[str] = field(default_factory=set)


def get_graph_info(graph: Graph) -> GraphInfo:
    """Get graph info.

    Parameters
    ----------
    graph : Graph
        The graph from which to get the info.

    Returns
    -------
    graph_info : GraphInfo
        The graph info.
    """
    number_of_nodes = graph.number_of_nodes()
    number_of_edges = graph.number_of_edges()
    unique_labels = {label for _, _, label in graph.edges.data(data="label")}

    return GraphInfo(number_of_nodes, number_of_edges, unique_labels)
