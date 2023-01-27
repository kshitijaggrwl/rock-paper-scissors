from abc import ABC,abstractmethod
from src.activity.Action import Action

class Player(ABC):
    """
    Base class for HumanPlayer and Computer Player class encapsulating common properties.
    Like Action performed, number of games won, lost or tied.
    """
    def __init__(self):
        """ Initializes the properties of the class"""
        self._action = [Action.ROCK, Action.PAPER, Action.SCISSOR]
        self._game_win = 0
        self._game_lose = 0
        self._game_count = 0

    @property 
    @abstractmethod
    def action(self):
        """
        Abstract getter method for action property of the class
        """
        return self._action_getter

    @property    
    def game_count(self):
        """
        Getter method for game_count property of the class
        """
        return self._game_count

    @game_count.setter
    def game_count(self, value):
        """
        Setter method for game_count property of the class
        """
        self._game_count = value

    @property
    def game_win(self):
        """
        Getter method for game_win property of the class
        """
        return self._game_win
    
    @game_win.setter
    def game_win(self, value):
        """
        Setter method for game_win property of the class
        """
        self._game_win = value

    @property
    def game_lose(self):
        """
        Getter method for game_lose property of the class
        """
        return self._game_lose
    
    @game_lose.setter
    def game_lose(self, value):
        """
        Setter method for game_lose property of the class
        """
        self._game_lose = value
    
