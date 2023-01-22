from activity.Action import Action
from exception.InvalidActionException import InvalidActionException
from result.Result import Result


class RockPaperScissor:

    @staticmethod
    def determine_winner(action_1: Action, action_2: Action):
        """
        Compares the user's action and the computer's action and returns the result of the round.
        
        Parameters:
            action_1 (Action): The user's selected action.
            action_2 (Action): The computer's selected action.
        
        Returns:
            Result: The result of the round. Can be TIE, LOSE, or WIN
        """
        if action_1 == action_2:
            return Result.TIE
            
        elif action_1 < action_2:
            return Result.LOSE
        
        elif action_1 > action_2:
            return Result.WIN    

            
            