class Dialer:
    __lower_limit = 0
    __upper_limit = 99

    def __init__(self, passing_point=0):
        self.reset()

        self.__passing_point = passing_point

    def reset(self):
        self._position = 50
        self._passing_point_count = 0

    def turn(self, turns):
        # No movement, no passings
        if turns == 0:
            return

        # Record the starting position to check for passings
        starting_position = self._position

        # Perform the turn
        self._position += turns

        # Wrap around - dialer is circular
        while self.__lower_limit > self._position or self._position > self.__upper_limit:
            if self._position < self.__lower_limit:
                # is + self.__position because at this point self._position is negative
                self._position = self.__upper_limit + (self._position + 1)
            elif self._position > self.__upper_limit:
                self._position = self.__lower_limit + (self._position - self.__upper_limit - 1)

            # if it wrapped, it passed the passing point
            if starting_position != self.__passing_point:
                self._passing_point_count += 0 if self._position == self.__passing_point else 1

    def position(self):
        return self._position

    def count_passings(self):
        return self._passing_point_count

    def lower_limit(self):
        return self.__lower_limit

    def upper_limit(self):
        return self.__upper_limit
