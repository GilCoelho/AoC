import pathlib
import sys

from aocd.models import Puzzle
from dotenv import load_dotenv

def is_movable_roll(grip_map, x, y, adjacent_limit_number=4, square_size=1, roll="@"):
    possible_x_pos = range(x - square_size, x + square_size+1)
    possible_y_pos = range(y - square_size, y + square_size+1)
    adjacent_elements = 0

    for check_x in possible_x_pos:
        for check_y in possible_y_pos:
            if check_x == x and check_y == y:
                # skip self
                continue

            if check_x < 0 or check_y < 0 or check_x >= len(grip_map) or check_y >= len(grip_map[0]):
                # skip out of bounds
                continue

            element = grip_map[check_x][check_y]
            if element == roll:
                adjacent_elements += 1

    return adjacent_elements < adjacent_limit_number

def parse(puzzle_input):
    """Parse input."""

    puzzle_input = puzzle_input.split() if isinstance(puzzle_input, str) else puzzle_input

    # Return a list of batteries banks
    return [list(puzzle_line) for puzzle_line in puzzle_input]

def part1(ranges):
    """Solve part 1."""
    new_map = [row.copy() for row in ranges]
    removed_roll = "x"
    roll = "@"
    num_of_removed_rolls = 0

    for x in range(len(new_map)):
        for y in range(len(new_map[0])):
            element = new_map[x][y]
            if element == roll:
                if is_movable_roll(ranges, x, y):
                    new_map[x][y] = removed_roll
                    num_of_removed_rolls += 1

    print("Number of removed rolls:", num_of_removed_rolls)

    return num_of_removed_rolls, new_map

def part2(ranges):
    """Solve part 2."""
    new_map = [row.copy() for row in ranges]
    removed_roll = "x"
    roll = "@"
    num_of_removed_rolls = 0

    for _ in range(len(new_map)*len(new_map[0])):
        prev_map = [row.copy() for row in new_map]
        got_rolls_removed = False

        for x in range(len(new_map)):
            for y in range(len(new_map[0])):
                element = new_map[x][y]
                if element == roll:
                    if is_movable_roll(prev_map, x, y):
                        new_map[x][y] = removed_roll
                        num_of_removed_rolls += 1
                        got_rolls_removed = True

        if not got_rolls_removed:
            break

    print("Number of removed rolls:", num_of_removed_rolls)

    return num_of_removed_rolls, new_map

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
        puzzle_input = Puzzle(year=2025, day=4).input_data

    # parse instructions
    grid_map = parse(puzzle_input)

    # solve part 1
    print("Solving part 1...")
    part1(grid_map)

    # solve part 2
    print("Solving part 2...")
    part2(grid_map)