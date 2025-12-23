import pytest

from aoc_2025 import main as aoc

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
    dialer = aoc.Dialer()

    # Starting position should be 50
    assert dialer.position() == dialer_start_pos

    dialer.turn(1)
    assert dialer.position() == 51
    dialer.turn(-2)
    assert dialer.position() == 49

def test_dialer_class_wrap_negative(dialer_lower_limit):
    """Test Dialer class negative move."""
    dialer = aoc.Dialer()

    # Lower limit should be 0
    assert dialer.lower_limit() == dialer_lower_limit

    dialer.turn(-1)
    assert dialer.position() == 49

    dialer.turn(-2)
    assert dialer.position() == 47

    dialer.turn(-47)
    assert dialer.position() == 0

    dialer.turn(-2)
    assert dialer.position() == 98

    dialer.turn(-100)
    assert dialer.position() == 98

    dialer.turn(-200)
    assert dialer.position() == 98

    dialer.turn(-1000)
    assert dialer.position() == 98

def test_dialer_class_wrap_positive(dialer_upper_limit):
    """Test Dialer class positive move."""
    dialer = aoc.Dialer()

    # Upper limit should be 99
    assert dialer.upper_limit() == dialer_upper_limit

    dialer.turn(1)
    assert dialer.position() == 51

    dialer.turn(2)
    assert dialer.position() == 53

    dialer.turn(46)
    assert dialer.position() == 99

    dialer.turn(2)
    assert dialer.position() == 1

    dialer.turn(100)
    assert dialer.position() == 1

    dialer.turn(200)
    assert dialer.position() == 1

    dialer.turn(1000)
    assert dialer.position() == 1
