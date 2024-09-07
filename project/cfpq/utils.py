import cfpq_data
from networkx import MultiDiGraph


def create_labeled_two_cycles_graph(
    first_cycle: tuple[int, str],
    second_cycle: tuple[int, str],
) -> MultiDiGraph:
    """Create labeled two cycles graph.

    Parameters
    ----------
    first_cycle : tuple[int, str]
        Number of nodes of the first circle and its edges label.
    second_cycle : tuple[int, str]
        Number of nodes of the second circle and its edges label.

    Returns
    -------
    graph : MultiDiGraph
        Created graph.
    """
    first_num_of_nodes, first_label = first_cycle
    second_num_of_nodes, second_label = second_cycle

    if first_num_of_nodes <= 0 or second_num_of_nodes <= 0:
        raise ValueError("Number of nodes must be positive")

    return cfpq_data.labeled_two_cycles_graph(
        n=first_num_of_nodes,
        m=second_num_of_nodes,
        labels=(first_label, second_label),
    )
