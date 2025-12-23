import pathlib
import sys

from aocd.models import Puzzle
from dotenv import load_dotenv


class Dialer:
    __lower_limit = 0
    __upper_limit = 99

    def __init__(self):
        self._position = 50

    def turn(self, turns):
        self._position += turns

        # Wrap around - dialer is circular
        while self.__lower_limit > self._position or self._position > self.__upper_limit:
            if self._position < self.__lower_limit:
                # is + self.__position because at this point self._position is negative
                self._position = self.__upper_limit + (self._position + 1)
            elif self._position > self.__upper_limit:
                self._position = self.__lower_limit + (self._position - self.__upper_limit - 1)

        print( f"Dialer turned {turns} to position {self._position}" )

    def position(self):
        return self._position

    def lower_limit(self):
        return self.__lower_limit

    def upper_limit(self):
        return self.__upper_limit

def parse(puzzle_input):
    """Parse input."""

    puzzle_input = puzzle_input.split() if isinstance(puzzle_input, str) else puzzle_input

    # Return a list of integers, negative for 'L' and positive for 'R' according to first character
    return [int(line[1:])*-1 if line[0] == 'L' else int(line[1:]) for line in puzzle_input]

def part1(turns):
    """Solve part 1."""
    counting_position = 0
    count = 0

    for action in turns:
        entrance_safe.turn(action)
        dialer_pos = entrance_safe.position()

        if counting_position == dialer_pos:
            count += 1

    print(f"The dialer stopped {count} times on the starting position.")

if __name__ == "__main__":
    entrance_safe = Dialer()
    puzzle_input = []

    # if command args are given, use them as input files
    if len(sys.argv) > 1:
        puzzle_input = pathlib.Path(sys.argv[1]).read_text().strip()
    else:
        # Environment variables load
        project_root = pathlib.Path(__file__).parent.parent.parent
        env_file = project_root / '.env'
        load_dotenv(env_file)

        # use personal input data from AoC
        puzzle_input = Puzzle(year=2025, day=1).input_data

    # parse instructions
    turns = parse(puzzle_input)

    # solve part 1
    part1(turns)
