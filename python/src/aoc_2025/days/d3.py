import pathlib
import sys

from aocd.models import Puzzle
from dotenv import load_dotenv

def bigger_combo_per_bank(bank, combo_size):
    """Return the biggest combination of given size in the bank string."""
    max_combo = ["" for _ in range(combo_size)]
    last_pos = 0

    for p in range(0, combo_size):
        last_biggest_num = 0
        range_limit = len(bank) - (combo_size - (p + 1))

        for i in range(last_pos, range_limit):
            eval_num = int(bank[i])

            if eval_num > last_biggest_num:
                last_biggest_num = eval_num
                max_combo[p] = last_biggest_num
                last_pos = i + 1

    return int(''.join(str(digit) for digit in max_combo))

def parse(puzzle_input):
    """Parse input."""

    puzzle_input = puzzle_input.split() if isinstance(puzzle_input, str) else puzzle_input

    # Return a list of batteries banks
    return puzzle_input

def part1(ranges):
    """Solve part 1."""
    total_joltage = 0
    for bank in ranges:
        total_joltage += bigger_combo_per_bank(bank, 2)

    print(f"The total joltage is {total_joltage} with 2 per bank.")
    return total_joltage

def part2(ranges):
    """Solve part 2."""
    total_joltage = 0
    combo_size = 12

    for bank in ranges:
        total_joltage += bigger_combo_per_bank(bank, combo_size)

    print(f"The total joltage is {total_joltage} with {combo_size} per bank.")
    return total_joltage

def main():
    puzzle_input = []

    # if command args are given, use them as input files
    if len(sys.argv) > 1:
        print("Loading input from file given as command line argument.")
        puzzle_input = pathlib.Path(sys.argv[1]).read_text().strip()
    else:
        print("Loading input from AoC website.")
        # Environment variables load
        project_root = pathlib.Path(__file__).parent.parent.parent.parent
        env_file = project_root / '.env'
        load_dotenv(env_file)

        # use personal input data from AoC
        puzzle_input = Puzzle(year=2025, day=3).input_data

    # parse instructions
    bats = parse(puzzle_input)

    # solve part 1
    print("Solving part 1...")
    part1(bats)

    # solve part 2
    print("Solving part 2...")
    part2(bats)