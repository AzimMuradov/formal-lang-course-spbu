import os
from dataclasses import astuple
from project.cfpq.cfpq import (
    create_and_save_labeled_two_cycles_graph_as_dot_file,
    load_graph_info_by_name,
)


def test_load_graph_info_by_name():
    (
        actual_number_of_nodes,
        actual_number_of_edges,
        actual_unique_labels,
    ) = astuple(load_graph_info_by_name("bzip"))

    assert 632 == actual_number_of_nodes
    assert 556 == actual_number_of_edges
    assert {"a", "d"} == actual_unique_labels


def test_create_and_save_labeled_two_cycles_graph_as_dot_file():
    curr_dir_path = os.path.dirname(os.path.realpath(__file__))
    expected_file_path = os.path.join(curr_dir_path, "test_cfpq_expected_graph.dot")
    actual_file_path = os.path.join(curr_dir_path, "test_cfpq_actual_graph.dot")

    assert create_and_save_labeled_two_cycles_graph_as_dot_file(
        first_cycle=(2, "a"),
        second_cycle=(2, "b"),
        path=actual_file_path,
    )

    with open(expected_file_path, "r") as expected_file:
        with open(actual_file_path, "r") as actual_file:
            assert expected_file.read() == actual_file.read()
