from agent.Player import Player
from activity.Action import Action
from exception.InvalidActionException import InvalidActionException

class HumanPlayer(Player):
    """
    A class representing a Human player in the game. 
    Inherits from the Player class and overrides the action property getter.
    """
    
    @Player.action.getter
    def action(self):
        """
        Getter property for the action of the player.
        Prompts the user to enter their choice of action (rock, paper, or scissors) and assigns the value to the self._action property.
        """
        user_input = int(input())
        if user_input not in [action.value for action in Action]:
            raise InvalidActionException(f"Invalid Input {user_input}")
        self._action = Action(user_input)
        return self._action
            
        