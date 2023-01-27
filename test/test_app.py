from src.activity.RockPaperScissor import RockPaperScissor
from src.agent.HumanPlayer import HumanPlayer
from src.agent.ComputerPlayer import ComputerPlayer
from src.result.Result import Result
from src.activity.Action import Action
from app import *

def test_process_result_tie():
    """
    Tests whether attributes of the player are updated successfully in case of tie
    """
    player1 = HumanPlayer()
    player2 = ComputerPlayer()
    action1 = Action.ROCK
    action2 = Action.ROCK
    process_result_tie(player1, player2, action1, action2)
    assert player1.game_count == 1
    assert player2.game_count == 1

def test_process_result_win():
    """
    Tests whether attributes of the player are updated successfully in case of win
    """
    player1 = HumanPlayer()
    player2 = ComputerPlayer()
    action1 = Action.ROCK
    action2 = Action.SCISSOR
    process_result_win(player1, player2, action1, action2)
    assert player1.game_count == 1
    assert player2.game_count == 1
    assert player1.game_win == 1
    assert player2.game_lose == 1

def test_process_result_lose():
    """
    Tests whether attributes of the player are updated successfully in case of loss
    """
    player1 = HumanPlayer()
    player2 = ComputerPlayer()
    action1 = Action.ROCK
    action2 = Action.PAPER
    process_result_lose(player1, player2, action1, action2)
    assert player1.game_count == 1
    assert player2.game_count == 1
    assert player1.game_lose == 1
    assert player2.game_win == 1
