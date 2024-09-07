from project.cfpq.graph_info import GraphInfo


def load_graph_info_by_name(name: str) -> GraphInfo:
    """Load a graph info by its name from the dataset.

    Parameters
    ----------
    name : str
        The name of the graph from the dataset.

    Returns
    -------
    graph : GraphInfo
        The graph info.
    """
    from project.cfpq.io import load_graph_by_name
    from project.cfpq.graph_info import get_graph_info

    return get_graph_info(load_graph_by_name(name))


def create_and_save_labeled_two_cycles_graph_as_dot_file(
    first_cycle: tuple[int, str],
    second_cycle: tuple[int, str],
    path: str,
) -> bool:
    """Create and save labeled two cycles graph as a dot file.

    Parameters
    ----------
    first_cycle : tuple[int, str]
        Number of nodes of the first circle and its edges label.
    second_cycle : tuple[int, str]
        Number of nodes of the second circle and its edges label.
    path: str
        The path where to save the file.

    Returns
    -------
    success : bool
        Returns True or False according to the success of the write operation.
    """
    from project.cfpq.utils import create_labeled_two_cycles_graph
    from project.cfpq.io import save_graph_as_dot_file

    graph = create_labeled_two_cycles_graph(first_cycle, second_cycle)

    return save_graph_as_dot_file(graph, path)
