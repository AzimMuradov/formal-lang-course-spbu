from typing import Set
from networkx import MultiDiGraph
from networkx.classes.reportviews import NodeDataView
from pyformlang.finite_automaton import (
    DeterministicFiniteAutomaton,
    NondeterministicFiniteAutomaton,
)
from pyformlang.regular_expression import Regex


def convert_regex_to_minimal_dfa(regex: str) -> DeterministicFiniteAutomaton:
    """Convert the given regular expression into a minimal DFA.

    Parameters
    ----------
    regex : str
        The regular expression to be converted into a minimal DFA.

    Returns
    -------
    minimal_dfa : DeterministicFiniteAutomaton
        Minimal deterministic finite automaton that is equivalent to the given regular expression.
    """
    return Regex(regex).to_epsilon_nfa().minimize()


def convert_graph_to_nfa(
    graph: MultiDiGraph,
    start_nodes: Set[int] = None,
    final_nodes: Set[int] = None,
) -> NondeterministicFiniteAutomaton:
    """Convert the given graph into a NFA.

    Parameters
    ----------
    graph : MultiDiGraph
        The graph to be converted. The imported graph requires to have the good format.
        Every valid edge should contain "label" data, invalid edges would be ignored.
        Some of the nodes may contain "is_start" or/and "is_final" data.
    start_nodes : Set[int]
        Optional start nodes for the automaton.
        If no start nodes provided and the given graph doesn't contain any node with "is_start" data,
        every node would be converted into a start node.
    final_nodes : Set[int]
        Optional final nodes for the automaton.
        If no final nodes provided and the given graph doesn't contain any node with "is_final" data,
        every node would be converted into a final node.

    Returns
    -------
    nfa : NondeterministicFiniteAutomaton
        Nondeterministic finite automaton that was built using the given parameters.
    """
    node_types = {"is_start": start_nodes, "is_final": final_nodes}

    for is_prop_str, nodes in node_types.items():
        if not nodes:
            view: NodeDataView = graph.nodes.data(data=is_prop_str, default=False)
            nodes = {} if any(is_prop for _, is_prop in view) else set(graph.nodes)
        for node in nodes:
            graph.nodes[node][is_prop_str] = True

    enfa = NondeterministicFiniteAutomaton.from_networkx(graph)
    return enfa.remove_epsilon_transitions()
