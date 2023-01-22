from src.agent.HumanPlayer import HumanPlayer
from src.activity.Action import Action
from src.exception.InvalidActionException import InvalidActionException

def test_human_player_valid_input():
    """
    Tests whether getter action method of HumanPlayer class generates valid action
    """
    human_player = HumanPlayer()
    human_player.action = lambda: 0
    assert human_player.action == Action.ROCK

    human_player.action = lambda: 1
    assert human_player.action == Action.PAPER

    human_player.action = lambda: 2
    assert human_player.action == Action.SCISSOR