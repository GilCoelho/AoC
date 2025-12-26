import pytest

from aoc_2025.days import d1 as aoc
from aoc_2025.modules.dialer import Dialer

@pytest.fixture
def example_data_from_page_d1p1():
    return "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"

@pytest.fixture
def example_data_from_page_d1p2():
    return "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"

@pytest.fixture
def example_data_1():
    return "L1\nR2\nL3"

@pytest.fixture
def dialer_start_pos():
    return 50

@pytest.fixture
def dialer_upper_limit():
    return 99

@pytest.fixture
def dialer_lower_limit():
    return 0

def test_parse_d1(example_data_1):
    """Test parsing of example input."""
    expected = [-1, 2, -3]
    result = aoc.parse(example_data_1)
    assert result == expected

def test_dialer_class_simple(dialer_start_pos):
    """Test Dialer class functionality."""
    dialer = Dialer()

    # Starting position should be 50
    assert dialer.position() == dialer_start_pos

    dialer.turn(1)
    assert dialer.position() == 51
    assert dialer.count_passings() == 0
    dialer.turn(-2)
    assert dialer.position() == 49
    assert dialer.count_passings() == 0

def test_dialer_class_wrap_negative(dialer_lower_limit):
    """Test Dialer class negative move."""
    dialer = Dialer()

    # Lower limit should be 0
    assert dialer.lower_limit() == dialer_lower_limit

    dialer.turn(-1)
    assert dialer.position() == 49
    assert dialer.count_passings() == 0

    dialer.turn(-2)
    assert dialer.position() == 47
    assert dialer.count_passings() == 0

    dialer.turn(-47)
    assert dialer.position() == 0
    assert dialer.count_passings() == 0

    dialer.turn(-2)
    assert dialer.position() == 98
    assert dialer.count_passings() == 0

    dialer.turn(-100)
    assert dialer.position() == 98
    assert dialer.count_passings() == 1

    dialer.turn(-200)
    assert dialer.position() == 98
    assert dialer.count_passings() == 3

    dialer.turn(-1000)
    assert dialer.position() == 98
    assert dialer.count_passings() == 13

def test_dialer_class_wrap_positive(dialer_upper_limit):
    """Test Dialer class positive move."""
    dialer = Dialer()

    # Upper limit should be 99
    assert dialer.upper_limit() == dialer_upper_limit

    dialer.turn(1)
    assert dialer.position() == 51
    assert dialer.count_passings() == 0

    dialer.turn(2)
    assert dialer.position() == 53
    assert dialer.count_passings() == 0

    dialer.turn(46)
    assert dialer.position() == 99
    assert dialer.count_passings() == 0

    dialer.turn(2)
    assert dialer.position() == 1
    assert dialer.count_passings() == 1

    dialer.turn(100)
    assert dialer.position() == 1
    assert dialer.count_passings() == 2

    dialer.turn(200)
    assert dialer.position() == 1
    assert dialer.count_passings() == 4

    dialer.turn(1000)
    assert dialer.position() == 1
    assert dialer.count_passings() == 14

def test_part1(example_data_1):
    """Test part 1 with example data."""
    turns = aoc.parse(example_data_1)
    dialer = Dialer()

    result = aoc.part1(dialer, turns)
    assert result == 0

    turns = [-48]
    result = aoc.part1(dialer, turns)
    assert result == 1

    turns = [99]
    result = aoc.part1(dialer, turns)
    assert result == 0

    turns = [5]
    result = aoc.part1(dialer, turns)
    assert result == 0

def test_part2(example_data_1):
    """Test part 2 with example data."""
    turns = aoc.parse(example_data_1)
    dialer = Dialer()

    result = aoc.part2(dialer, turns)
    assert result == 0

    turns = [-48]
    dialer = Dialer() # reset dialer
    result = aoc.part2(dialer, turns)
    assert result == 0

    turns = [99]
    dialer = Dialer() # reset dialer
    result = aoc.part2(dialer, turns)
    assert result == 1

    turns = [50]
    dialer = Dialer() # reset dialer
    result = aoc.part2(dialer, turns)
    assert result == 1

def test_part1_from_page(example_data_from_page_d1p1):
    """Test part 1 with example data from the page."""
    turns = aoc.parse(example_data_from_page_d1p1)
    dialer = Dialer()

    result = aoc.part1(dialer, turns)
    assert result == 3

def test_part2_from_page(example_data_from_page_d1p2):
    """Test part 2 with example data from the page."""
    turns = aoc.parse(example_data_from_page_d1p2)
    dialer = Dialer()
    result = aoc.part2(dialer, turns)
    assert result == 6

    turns.insert(0, 18)
    result = aoc.part2(dialer, turns)
    assert result == 9

    result = aoc.part2(dialer, turns)
    assert result == 12

    dialer = Dialer()
    result = aoc.part2(dialer, [1000])
    assert result == 10

    dialer = Dialer()
    result = aoc.part2(dialer, [-1000])
    assert result == 10

    dialer = Dialer()
    result = aoc.part2(dialer, [1000, -1000])
    assert result == 20
