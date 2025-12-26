import pytest

from aoc_2025.days import d2 as aoc

@pytest.fixture
def example_data_from_page_d2p1():
    return "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def test_parse_example_data_from_page_d2p1(example_data_from_page_d2p1):
    """Test parsing of example data from AoC page for day 2, part 1."""
    parsed = aoc.parse(example_data_from_page_d2p1)
    assert parsed == [['11', '22'], ['95', '115'], ['998', '1012'], ['1188511880', '1188511890'], ['222220', '222224'], ['1698522', '1698528'], ['446443', '446449'], ['38593856', '38593862'], ['565653', '565659'], ['824824821', '824824827'], ['2121212118', '2121212124']]

def test_is_sequence_digits_twice():
    """Test is_sequence_digits_twice function."""
    assert aoc.is_sequence_digits_twice(1212) is True
    assert aoc.is_sequence_digits_twice(123123) is True
    assert aoc.is_sequence_digits_twice(1234) is False
    assert aoc.is_sequence_digits_twice(12345) is False
    assert aoc.is_sequence_digits_twice(1111) is True
    assert aoc.is_sequence_digits_twice(22) is True
    assert aoc.is_sequence_digits_twice(7) is False
    assert aoc.is_sequence_digits_twice(99) is True
    assert aoc.is_sequence_digits_twice(1010) is True
    assert aoc.is_sequence_digits_twice(1312) is False
    assert aoc.is_sequence_digits_twice(1231123) is False

def test_part1_from_page(example_data_from_page_d2p1):
    """Test part 1 with example data from AoC page."""
    ranges = aoc.parse(example_data_from_page_d2p1)
    result = aoc.part1(ranges)
    assert result == 1227775554