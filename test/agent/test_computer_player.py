from src.agent.ComputerPlayer import ComputerPlayer
from src.activity.Action import Action

def test_computer_player_action_valid():
    """
    Tests whether getter action method of ComputerPlayer class generates valid action
    """
    computer_player = ComputerPlayer()
    action = computer_player.action
    assert action in list(Action)

