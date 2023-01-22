from src.activity.RockPaperScissor import RockPaperScissor
from src.result.Result import Result
from src.activity.Action import Action

def test_determine_winner():
    """
    Tests determine_winner method of Rock Paper Scissor class for all possible inputs
    """
    assert (RockPaperScissor.determine_winner(Action.ROCK, Action.ROCK) == Result.TIE) == True
    assert (RockPaperScissor.determine_winner(Action.ROCK, Action.PAPER) == Result.LOSE) == True
    assert (RockPaperScissor.determine_winner(Action.ROCK, Action.SCISSOR) == Result.WIN) == True
    assert (RockPaperScissor.determine_winner(Action.PAPER, Action.ROCK) == Result.WIN) == True
    assert (RockPaperScissor.determine_winner(Action.PAPER, Action.PAPER) == Result.TIE) == True
    assert (RockPaperScissor.determine_winner(Action.PAPER, Action.SCISSOR) == Result.LOSE) == True
    assert (RockPaperScissor.determine_winner(Action.SCISSOR, Action.ROCK) == Result.LOSE) == True
    assert (RockPaperScissor.determine_winner(Action.SCISSOR, Action.PAPER) == Result.WIN) == True
    assert (RockPaperScissor.determine_winner(Action.SCISSOR, Action.SCISSOR) == Result.TIE) == True
