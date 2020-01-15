import pytest
from treasure_hunt.oop_implementation import find_treasure


def test_find_treasure(treasure_map_and_expected_path):
    treasure_map, expected_path = treasure_map_and_expected_path
    print(treasure_map, expected_path)
    assert find_treasure(treasure_map) == expected_path


def test_find_treasure_without_treasure(treasure_map_without_treasure):
    with pytest.raises(ValueError):
        find_treasure(treasure_map_without_treasure)


def test_find_treasure_with_infinite_loop(treasure_map_with_infinite_loop):
    with pytest.raises(ValueError):
        find_treasure(treasure_map_with_infinite_loop)
