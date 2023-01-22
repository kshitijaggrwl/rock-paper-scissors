from enum import IntEnum

class Action(IntEnum):
    """
    Enum class representing the possible actions in a game of rock-paper-scissors.
    """

    ROCK = 0
    PAPER = 1
    SCISSOR = 2

    def __eq__(self, other):
        """
        Overrides the default implementation of the equality operator for the Action class.
        Two Action objects are considered equal if their names are the same.
        """
        if self.name == other.name:
            return True
        else:
            return False

    def __gt__(self, other):
        """
        Overrides the default implementation of the greater than operator for the Action class.
        An Action object is considered greater than another Action object if it wins against it in a game of rock-paper-scissors.
        """
        if self.name == "ROCK":
            if other.name == "SCISSOR":
                return True
            else:
                return False
        elif self.name == "PAPER":
            if other.name == "ROCK":
                return True
            else:
                return False
        elif self.name == "SCISSOR":
            if other.name == "PAPER":
                return True
            else:
                return False

    def __lt__(self, other):
        """
        Overrides the default implementation of the less than operator for the Action class.
        An Action object is considered less than another Action object if it loses against it in a game of rock-paper-scissors.
        """
        if self.name == "ROCK":
            if other.name == "PAPER":
                return True
            else:
                return False
        elif self.name == "PAPER":
            if other.name == "SCISSOR":
                return True
            else:
                return False
        elif self.name == "SCISSOR":
            if other.name == "ROCK":
                return True
            else:
                return False