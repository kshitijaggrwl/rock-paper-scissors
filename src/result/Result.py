from enum import IntEnum

class Result(IntEnum):
    """
    Enum class representing the possible results in the game of rock-paper-scissors.
    """
    TIE = 0
    WIN = 1
    LOSE = 2