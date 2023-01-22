class GameError(Exception):
    """
    Base exception for game related errors
    """
    pass

class InvalidChoiceError(GameError):
    """
    Exception raised when an invalid choice is entered
    """
    pass