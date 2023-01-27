from src.agent.HumanPlayer import HumanPlayer
from src.activity.Action import Action
from src.exception.InvalidActionException import InvalidActionException

def test_human_player_valid_input():
    """
    Tests whether getter action method of HumanPlayer class generates valid action
    """
    human_player = HumanPlayer()
    action = Action(0)
    assert action == Action.ROCK

    action = Action(1)
    assert action == Action.PAPER

    action = Action(2)
    assert action == Action.SCISSOR