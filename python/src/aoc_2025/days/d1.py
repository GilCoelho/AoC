import pathlib
import sys

from aocd.models import Puzzle
from dotenv import load_dotenv

from ..modules.dialer import Dialer


def parse(puzzle_input):
    """Parse input."""

    puzzle_input = puzzle_input.split() if isinstance(puzzle_input, str) else puzzle_input

    # Return a list of integers, negative for 'L' and positive for 'R' according to first character
    return [int(line[1:])*-1 if line[0] == 'L' else int(line[1:]) for line in puzzle_input]

def part1(entrance_safe, turns):
    """Solve part 1."""
    counting_position = 0
    count = 0

    for action in turns:
        entrance_safe.turn(action)
        dialer_pos = entrance_safe.position()

        if counting_position == dialer_pos:
            count += 1

    print(f"The dialer stopped {count} times on the starting position.")
    return count

def part2(entrance_safe, turns):
    """Solve part 2."""
    counting_position = 0
    count = 0

    for action in turns:
        entrance_safe.turn(action)
        dialer_pos = entrance_safe.position()

        if counting_position == dialer_pos:
            count += 1

    count += entrance_safe.count_passings()

    print(f"The dialer stopped and passed by 0 {count} times.")
    return count

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
        puzzle_input = Puzzle(year=2025, day=1).input_data

    # parse instructions
    turns = parse(puzzle_input)

    # solve part 1
    entrance_safe_1 = Dialer()
    part1(entrance_safe_1, turns)

    # solve part 2
    entrance_safe_2 = Dialer()
    part2(entrance_safe_2, turns)
