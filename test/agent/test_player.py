from src.activity.Action import Action
from src.agent.Player import Player

Player.__abstractmethods__ = set()
def test_player_init():
    """
    Tests whether attributes of the player class are initialised properly
    """
    player = Player()
    assert player._action == [Action.ROCK, Action.PAPER, Action.SCISSOR]
    assert player._game_win == 0
    assert player._game_lose == 0
    assert player._game_count == 0

def test_player_property_game_count():
    """
    Tests whether setter method of the game_count attribute is working or not
    """
    player = Player()
    player.game_count = 5
    assert player.game_count == 5

def test_player_property_game_win():
    """
    Tests whether setter method of the game_win attribute is working or not
    """
    player = Player()
    player.game_win = 2
    assert player.game_win == 2

def test_player_property_game_lose():
    """
    Tests whether setter method of the game_lose attribute is working or not
    """
    player = Player()
    player.game_lose = 1
    assert player.game_lose == 1

