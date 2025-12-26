import pytest

from aoc_2025.days import d3 as aoc

@pytest.fixture
def example_data_from_page_d3p1():
    return "987654321111111\n811111111111119\n234234234234278\n818181911112111"

def test_parse_example_data_from_page_d3p1(example_data_from_page_d3p1):
    """Test parsing of example data from AoC page for day 3, part 1."""
    parsed = aoc.parse(example_data_from_page_d3p1)
    assert parsed == ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]

    parsed = aoc.parse(["987654321111111", "811111111111119", "234234234234278", "818181911112111"])
    assert parsed == ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]

def test_bigger_combo_per_bank():
    combo_size = 2
    assert aoc.bigger_combo_per_bank("987654321111111", combo_size) == 98
    assert aoc.bigger_combo_per_bank("811111119111111", combo_size) == 91
    assert aoc.bigger_combo_per_bank("811111111111819", combo_size) == 89
    assert aoc.bigger_combo_per_bank("811111111111189", combo_size) == 89
    assert aoc.bigger_combo_per_bank("811111111111119", combo_size) == 89
    assert aoc.bigger_combo_per_bank("234234234234278", combo_size) == 78
    assert aoc.bigger_combo_per_bank("818181911112111", combo_size) == 92
    assert aoc.bigger_combo_per_bank("111111111111119", combo_size) == 19

    assert aoc.bigger_combo_per_bank("498953", combo_size) == 99

    assert aoc.bigger_combo_per_bank("4468455455454384872948296641655953578334969369425239274865655978655569965666183954746455448625424753", combo_size) == 99
    assert aoc.bigger_combo_per_bank("4368254754644555445525653536457444356537652556558555754544544553466455574455756245445766555525335645", combo_size) == 88

    combo_size = 3
    assert aoc.bigger_combo_per_bank("987118", combo_size) == 988
    assert aoc.bigger_combo_per_bank("987654321111111", combo_size) == 987
    assert aoc.bigger_combo_per_bank("811111119111111", combo_size) == 911
    assert aoc.bigger_combo_per_bank("234234234234278", combo_size) == 478
    assert aoc.bigger_combo_per_bank("818181911112111", combo_size) == 921

    combo_size = 12
    assert aoc.bigger_combo_per_bank("987654321111111", combo_size) == 987654321111
    assert aoc.bigger_combo_per_bank("811111111111119", combo_size) == 811111111119
    assert aoc.bigger_combo_per_bank("234234234234278", combo_size) == 434234234278
    assert aoc.bigger_combo_per_bank("818181911112111", combo_size) == 888911112111

def test_part1_from_page(example_data_from_page_d3p1):
    """Test part 1 with example data from AoC page for day 3, part 1."""
    banks = aoc.parse(example_data_from_page_d3p1)
    result = aoc.part1(banks)
    assert result == 357

def test_part2_from_page(example_data_from_page_d3p1):
    """Test part 2 with example data from AoC page for day 3, part 2."""
    banks = aoc.parse(example_data_from_page_d3p1)
    result = aoc.part2(banks)
    assert result == 3121910778619
