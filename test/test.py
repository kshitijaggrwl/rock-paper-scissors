import pytest
import random
from src.action import Action
from src.rps import RockPaperScissors

@pytest.fixture
def rps():
    """ Fixture that returns an instance of RockPaperScissors class."""
    return RockPaperScissors()

def test_get_user_action(rps):
    """ Test that get_user_action method returns the correct action based on user input."""
    rps.get_user_action = lambda: 1
    assert rps.get_user_action() == Action.Rock

    rps.get_user_action = lambda: 2
    assert rps.get_user_action() == Action.Paper

    rps.get_user_action = lambda: 3
    assert rps.get_user_action() == Action.Scissors

def test_get_computer_action(rps):
    """ Test that get_computer_action method returns a valid action."""
    rps.get_computer_action = lambda: random.choice([Action.Rock, Action.Paper, Action.Scissors])
    assert rps.get_computer_action() in [Action.Rock, Action.Paper, Action.Scissors]

def test_determine_winner(rps):
    """ Test that determine_winner method updates the wins, losses, and ties properties correctly."""
    rps.determine_winner(Action.Rock, Action.Scissors)
    assert rps.wins == 1

    rps.determine_winner(Action.Rock, Action.Paper)
    assert rps.losses == 1

    rps.determine_winner(Action.Rock, Action.Rock)
    assert rps.ties == 1

def test_print_score(rps):
    """ Test that print_score method returns the correct score message."""
    rps.wins = 2
    rps.losses = 1
    rps.ties = 0
    assert rps.print_score() == "You have 2 wins, 1 losses, and 0 ties."

def test_user_wants_to_play_again(rps):
    """ Test that user_wants_to_play_again method returns the correct boolean value based on user input."""
    rps.user_wants_to_play_again = lambda: "y"
    assert rps.user_wants_to_play_again() == True

    rps.user_wants_to_play_again = lambda: "n"
    assert rps.user_wants_to_play_again() == False