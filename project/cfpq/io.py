import cfpq_data
from networkx import Graph, MultiDiGraph


def load_graph_by_name(name: str) -> MultiDiGraph:
    """Load a graph by its name from the dataset.

    Parameters
    ----------
    name : str
        The name of the graph from the dataset.

    Returns
    -------
    graph : MultiDiGraph
        The graph data.
    """
    return cfpq_data.graph_from_csv(path=(cfpq_data.download(name)))


def save_graph_as_dot_file(graph: Graph, path: str) -> bool:
    """Save the graph to the provided path.

    Parameters
    ----------
    graph : Graph
        The name of the graph from the dataset.
    path : str
        The path where to save the file.

    Returns
    -------
    success : bool
        Returns True or False according to the success of the write operation.
    """
    from networkx.drawing.nx_pydot import to_pydot as graph_to_dot

    return graph_to_dot(graph).write(path)
