import pytest

from aoc_2025.days import d4 as aoc

@pytest.fixture
def example_data_from_page_d4p1():
    return """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

def test_parse_example_data_from_page_d4p1(example_data_from_page_d4p1):
    """Test parsing of example data from AoC page for day 4, part 1."""
    parsed = aoc.parse(example_data_from_page_d4p1)
    assert parsed == [[".", ".", "@", "@", ".", "@", "@", "@", "@", "."],
                      ["@", "@", "@", ".", "@", ".", "@", ".", "@", "@"],
                      ["@", "@", "@", "@", "@", ".", "@", ".", "@", "@"],
                      ["@", ".", "@", "@", "@", "@", ".", ".", "@", "."],
                      ["@", "@", ".", "@", "@", "@", "@", ".", "@", "@"],
                      [".", "@", "@", "@", "@", "@", "@", "@", ".", "@"],
                      [".", "@", ".", "@", ".", "@", ".", "@", "@", "@"],
                      ["@", ".", "@", "@", "@", ".", "@", "@", "@", "@"],
                      [".", "@", "@", "@", "@", "@", "@", "@", "@", "."],
                      ["@", ".", "@", ".", "@", "@", "@", ".", "@", "."]]

def test_is_movable_roll(example_data_from_page_d4p1):
    """Test is_movable_roll function with example data from AoC page for day 4, part 1."""
    grip_map = aoc.parse(example_data_from_page_d4p1)

    assert aoc.is_movable_roll(grip_map, 0, 2) is True
    assert aoc.is_movable_roll(grip_map, 1, 1) is False
    assert aoc.is_movable_roll(grip_map, 4, 4) is False

def test_part1_from_page(example_data_from_page_d4p1):
    """Test part 1 solution with example data from AoC page for day 4, part 1."""
    grip_map = aoc.parse(example_data_from_page_d4p1)

    result, new_map = aoc.part1(grip_map)

    expected_result = [ [".", ".", "x", "x", ".", "x", "x", "@", "x", "."],
                        ["x", "@", "@", ".", "@", ".", "@", ".", "@", "@"],
                        ["@", "@", "@", "@", "@", ".", "x", ".", "@", "@"],
                        ["@", ".", "@", "@", "@", "@", ".", ".", "@", "."],
                        ["x", "@", ".", "@", "@", "@", "@", ".", "@", "x"],
                        [".", "@", "@", "@", "@", "@", "@", "@", ".", "@"],
                        [".", "@", ".", "@", ".", "@", ".", "@", "@", "@"],
                        ["x", ".", "@", "@", "@", ".", "@", "@", "@", "@"],
                        [".", "@", "@", "@", "@", "@", "@", "@", "@", "."],
                        ["x", ".", "x", ".", "@", "@", "@", ".", "x", "."]]

    assert result == 13
    assert new_map == expected_result
