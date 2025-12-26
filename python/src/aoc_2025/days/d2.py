import pathlib
import sys

from aocd.models import Puzzle
from dotenv import load_dotenv

def is_sequence_digits_twice(num):
    """Check if a sequence contains some sequence of digits repeated twice."""
    value = str(num)
    if len(value) % 2 != 0:
        # if length is odd, cannot be made of two same halves
        return False
    else:
        # length is even, compare two halves
        mid = len(value) // 2
        return value[:mid] == value[mid:]

def is_sequence_digits_repeated(num):
    """Check if a sequence contains some sequence of digits repeated."""
    value = str(num)
    is_repeated = False

    for i in range(1, len(value)):
        is_section_repeated = True
        # pick a section length i
        section = value[:i]
        for j in range(i, len(value), i):
            if value[j:j+i] == section:
                is_section_repeated &= True
            else:
                # break inner loop if no match
                is_section_repeated &= False
                break
        is_repeated |= is_section_repeated

    return is_repeated

def parse(puzzle_input):
    """Parse input."""

    puzzle_input = puzzle_input.split(',') if isinstance(puzzle_input, str) else puzzle_input

    # Return a list of intervals, [[start, end], [start, end], ...]
    return [line.split('-') for line in puzzle_input]

def part1(ranges):
    """Solve part 1."""
    sum_of_invalid_ids = 0
    for start, end in ranges:
        start_num = int(start)
        end_num = int(end)
        for num in range(start_num, end_num + 1):
            if is_sequence_digits_twice(num):
                sum_of_invalid_ids += num

    print(f"The sum of all invalid product IDs is {sum_of_invalid_ids}.")
    return sum_of_invalid_ids

def part2(ranges):
    """Solve part 2."""
    sum_of_invalid_ids = 0
    for start, end in ranges:
        start_num = int(start)
        end_num = int(end)
        for num in range(start_num, end_num + 1):
            if is_sequence_digits_repeated(num):
                sum_of_invalid_ids += num

    print(f"The sum of all invalid product IDs is {sum_of_invalid_ids}.")
    return sum_of_invalid_ids

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
        puzzle_input = Puzzle(year=2025, day=2).input_data

    # parse instructions
    ranges = parse(puzzle_input)

    # solve part 1
    print("Solving part 1...")
    part1(ranges)

    # solve part 2
    print("Solving part 2...")
    part2(ranges)
