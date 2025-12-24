class Dialer:
    __lower_limit = 0
    __upper_limit = 99

    __passing_point = 0

    def __init__(self, passing_point=0):
        self._position = 50
        self._passing_point_count = 0

    def turn(self, turns):
        self._position += turns

        # Wrap around - dialer is circular
        while self.__lower_limit > self._position or self._position > self.__upper_limit:
            if self._position < self.__lower_limit:
                # is + self.__position because at this point self._position is negative
                self._position = self.__upper_limit + (self._position + 1)
                # if it wrapped, it passed the passing point
                self._passing_point_count += 1
            elif self._position > self.__upper_limit:
                self._position = self.__lower_limit + (self._position - self.__upper_limit - 1)
                # if it wrapped, it passed the passing point
                self._passing_point_count += 1

        # if it lands exactly on the passing point, remove one passing count
        if self._position == self.__passing_point and self._passing_point_count >= 1:
            self._passing_point_count -= 1

        #print( f"Dialer turned {turns} to position {self._position}" )

    def position(self):
        return self._position

    def count_passings(self):
        return self._passing_point_count

    def lower_limit(self):
        return self.__lower_limit

    def upper_limit(self):
        return self.__upper_limit
