from networkx import MultiDiGraph
from pyformlang.finite_automaton import (
    DeterministicFiniteAutomaton,
    NondeterministicFiniteAutomaton,
)
from project.automata.converters import (
    convert_regex_to_minimal_dfa,
    convert_graph_to_nfa,
)


def test_convert_regex_to_minimal_dfa_empty():
    actual = convert_regex_to_minimal_dfa("")
    expected = DeterministicFiniteAutomaton()
    assert expected == actual


def test_convert_regex_to_minimal_dfa_a_star():
    actual = convert_regex_to_minimal_dfa("a*")
    expected = DeterministicFiniteAutomaton()
    expected.add_start_state(1)
    expected.add_final_state(1)
    expected.add_transitions([(1, "a", 1)])
    assert expected == actual
    assert actual.is_deterministic()
    assert len(actual.states) == len(actual.minimize().states)


def test_convert_regex_to_minimal_dfa_a_or_b():
    actual = convert_regex_to_minimal_dfa("a|b")
    expected = DeterministicFiniteAutomaton()
    expected.add_start_state(1)
    expected.add_final_state(2)
    expected.add_transitions([(1, "a", 2), (1, "b", 2)])
    assert expected == actual
    assert actual.is_deterministic()
    assert len(actual.states) == len(actual.minimize().states)


def test_convert_graph_to_nfa_empty():
    graph = MultiDiGraph()
    actual = convert_graph_to_nfa(graph)
    expected = NondeterministicFiniteAutomaton()
    assert expected == actual


def test_convert_graph_to_nfa_without_labels():
    graph = MultiDiGraph([(1, 2), (2, 3)])
    actual = convert_graph_to_nfa(graph)
    expected = NondeterministicFiniteAutomaton()
    for s in range(1, 4):
        expected.add_start_state(s)
        expected.add_final_state(s)
    assert expected == actual


def test_convert_graph_to_nfa_with_labels():
    graph = MultiDiGraph([(1, 2, {"label": "a"}), (2, 3, {"label": "b"})])
    actual = convert_graph_to_nfa(graph)
    expected = NondeterministicFiniteAutomaton()
    for s in range(1, 4):
        expected.add_start_state(s)
        expected.add_final_state(s)
    expected.add_transitions([(1, "a", 2), (2, "b", 3)])
    assert expected == actual


def test_convert_graph_to_nfa_with_start_nodes():
    graph = MultiDiGraph([(1, 2), (2, 3)])
    actual = convert_graph_to_nfa(graph, start_nodes={1})
    expected = NondeterministicFiniteAutomaton()
    expected.add_start_state(1)
    for s in range(1, 4):
        expected.add_final_state(s)
    assert expected == actual


def test_convert_graph_to_nfa_with_final_nodes():
    graph = MultiDiGraph([(1, 2), (2, 3)])
    actual = convert_graph_to_nfa(graph, final_nodes={1})
    expected = NondeterministicFiniteAutomaton()
    expected.add_final_state(1)
    for s in range(1, 4):
        expected.add_start_state(s)
    assert expected == actual


def test_convert_graph_to_nfa_with_graph_start_nodes():
    graph = MultiDiGraph([(1, 2), (2, 3)])
    graph.add_node(1, is_start=True)
    actual = convert_graph_to_nfa(graph)
    expected = NondeterministicFiniteAutomaton()
    expected.add_start_state(1)
    for s in range(1, 4):
        expected.add_final_state(s)
    assert expected == actual


def test_convert_graph_to_nfa_with_graph_final_nodes():
    graph = MultiDiGraph([(1, 2), (2, 3)])
    graph.add_node(1, is_final=True)
    actual = convert_graph_to_nfa(graph)
    expected = NondeterministicFiniteAutomaton()
    expected.add_final_state(1)
    for s in range(1, 4):
        expected.add_start_state(s)
    assert expected == actual


def test_convert_graph_to_nfa_with_various_start_nodes():
    graph = MultiDiGraph([(1, 2), (2, 3)])
    graph.add_node(1, is_start=True)
    actual = convert_graph_to_nfa(graph, start_nodes={3})
    expected = NondeterministicFiniteAutomaton()
    expected.add_start_state(1)
    expected.add_start_state(3)
    for s in range(1, 4):
        expected.add_final_state(s)
    assert expected == actual


def test_convert_graph_to_nfa_with_various_final_nodes():
    graph = MultiDiGraph([(1, 2), (2, 3)])
    graph.add_node(1, is_final=True)
    actual = convert_graph_to_nfa(graph, final_nodes={3})
    expected = NondeterministicFiniteAutomaton()
    expected.add_final_state(1)
    expected.add_final_state(3)
    for s in range(1, 4):
        expected.add_start_state(s)
    assert expected == actual
