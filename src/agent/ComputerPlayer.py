from random import choice
from agent.Player import Player
from activity.Action import Action

class ComputerPlayer(Player):
    """
    A ComputerPlayer class that extends the Player class and overrides the action property getter
    to return a random choice from the list of Action enums.
    """
    
    @Player.action.getter
    def action(self):
        """
        Returns a random action from the list of Action enums
        """
        self._action = choice(list(Action)) 
        return self._action