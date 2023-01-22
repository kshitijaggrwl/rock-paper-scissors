import pytest
from src.activity.Action import Action
from src.agent.Player import Player

def test_player_init(player):
    """
    Tests whether attributes of the player class are initialised properly
    """
    assert player._action == [Action.ROCK, Action.PAPER, Action.SCISSOR]
    assert player._game_win == 0
    assert player._game_lose == 0
    assert player._game_count == 0

def test_player_property_game_count(player):
    """
    Tests whether setter method of the game_count attribute is working or not
    """
    player.game_count = 5
    assert player.game_count == 5

def test_player_property_game_win(player):
    """
    Tests whether setter method of the game_win attribute is working or not
    """
    player.game_win = 2
    assert player.game_win == 2

def test_player_property_game_lose(player):
    """
    Tests whether setter method of the game_lose attribute is working or not
    """
    player.game_lose = 1
    assert player.game_lose == 1


@pytest.fixture
def player():
    return Player()
