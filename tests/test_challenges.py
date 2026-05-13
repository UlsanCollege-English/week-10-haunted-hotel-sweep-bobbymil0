"""Tests for Week 10 Coding #8: Haunted Hotel Sweep."""

from src.challenges import (
    bfs_order,
    count_reachable_areas,
    dfs_order,
    get_neighbors,
    has_path,
)


HAUNTED_HOTEL = {
    "Lobby": ["Hallway", "Dining Room"],
    "Hallway": ["Lobby", "Library", "Stairs"],
    "Dining Room": ["Lobby", "Kitchen"],
    "Kitchen": ["Dining Room", "Cellar"],
    "Cellar": ["Kitchen", "Library"],
    "Library": ["Hallway", "Cellar"],
    "Stairs": ["Hallway", "Tower"],
    "Tower": ["Stairs"],
    # Disconnected locked wing:
    "Locked Wing": ["Mirror Room"],
    "Mirror Room": ["Locked Wing"],
    # Isolated area:
    "Attic": [],
}


def test_get_neighbors_existing_area():
    assert get_neighbors(HAUNTED_HOTEL, "Lobby") == ["Hallway", "Dining Room"]


def test_get_neighbors_missing_area_returns_empty_list():
    assert get_neighbors(HAUNTED_HOTEL, "Ballroom") == []


def test_get_neighbors_area_with_no_neighbors():
    assert get_neighbors(HAUNTED_HOTEL, "Attic") == []


def test_has_path_returns_true_for_reachable_target():
    assert has_path(HAUNTED_HOTEL, "Lobby", "Tower") is True


def test_has_path_returns_false_for_disconnected_target():
    assert has_path(HAUNTED_HOTEL, "Lobby", "Mirror Room") is False


def test_has_path_returns_false_for_missing_start():
    assert has_path(HAUNTED_HOTEL, "Ballroom", "Tower") is False


def test_has_path_returns_false_for_missing_target():
    assert has_path(HAUNTED_HOTEL, "Lobby", "Ballroom") is False


def test_has_path_start_equals_target_existing_area():
    assert has_path(HAUNTED_HOTEL, "Lobby", "Lobby") is True


def test_has_path_start_equals_target_missing_area():
    assert has_path(HAUNTED_HOTEL, "Ballroom", "Ballroom") is False


def test_bfs_order_from_lobby():
    assert bfs_order(HAUNTED_HOTEL, "Lobby") == [
        "Lobby",
        "Hallway",
        "Dining Room",
        "Library",
        "Stairs",
        "Kitchen",
        "Cellar",
        "Tower",
    ]


def test_bfs_order_missing_start_returns_empty_list():
    assert bfs_order(HAUNTED_HOTEL, "Ballroom") == []


def test_bfs_order_disconnected_component():
    assert bfs_order(HAUNTED_HOTEL, "Locked Wing") == [
        "Locked Wing",
        "Mirror Room",
    ]


def test_bfs_order_area_with_no_neighbors():
    assert bfs_order(HAUNTED_HOTEL, "Attic") == ["Attic"]


def test_dfs_order_from_lobby():
    assert dfs_order(HAUNTED_HOTEL, "Lobby") == [
        "Lobby",
        "Hallway",
        "Library",
        "Cellar",
        "Kitchen",
        "Dining Room",
        "Stairs",
        "Tower",
    ]


def test_dfs_order_missing_start_returns_empty_list():
    assert dfs_order(HAUNTED_HOTEL, "Ballroom") == []


def test_dfs_order_area_with_no_neighbors():
    assert dfs_order(HAUNTED_HOTEL, "Attic") == ["Attic"]


def test_traversals_handle_cycle_without_revisiting():
    cycle_graph = {
        "A": ["B", "C"],
        "B": ["A", "C"],
        "C": ["A", "B"],
    }

    assert has_path(cycle_graph, "A", "C") is True
    assert bfs_order(cycle_graph, "A") == ["A", "B", "C"]
    assert dfs_order(cycle_graph, "A") == ["A", "B", "C"]


def test_empty_graph_behavior():
    graph = {}

    assert get_neighbors(graph, "Lobby") == []
    assert has_path(graph, "Lobby", "Tower") is False
    assert bfs_order(graph, "Lobby") == []
    assert dfs_order(graph, "Lobby") == []


# Stretch tests. These are included so students who complete the stretch
# can verify their function. If you do not want to grade the stretch function,
# you may remove these tests before publishing.

def test_count_reachable_areas_from_lobby_stretch():
    assert count_reachable_areas(HAUNTED_HOTEL, "Lobby") == 8


def test_count_reachable_areas_missing_start_stretch():
    assert count_reachable_areas(HAUNTED_HOTEL, "Ballroom") == 0
