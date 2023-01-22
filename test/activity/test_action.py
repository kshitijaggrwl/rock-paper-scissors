from src.activity.Action import Action

def test_action_eq():
    """
    Tests overloaded == operator on Action Enum for all possible scenarios 
    """
    assert (Action.ROCK == Action.ROCK) == True
    assert (Action.ROCK == Action.PAPER) == False
    assert (Action.ROCK == Action.SCISSOR) == False
    assert (Action.PAPER == Action.ROCK) == False
    assert (Action.PAPER == Action.PAPER) == True
    assert (Action.PAPER == Action.SCISSOR) == False
    assert (Action.SCISSOR == Action.ROCK) == False
    assert (Action.SCISSOR == Action.PAPER) == False
    assert (Action.SCISSOR == Action.SCISSOR) == True

def test_action_gt():
    """
    Tests overloaded > operator on Action Enum for all possible scenarios 
    """
    assert (Action.ROCK > Action.ROCK) == False
    assert (Action.ROCK > Action.PAPER) == False
    assert (Action.ROCK > Action.SCISSOR) == True
    assert (Action.PAPER > Action.ROCK) == True
    assert (Action.PAPER > Action.PAPER) == False
    assert (Action.PAPER > Action.SCISSOR) == False
    assert (Action.SCISSOR > Action.ROCK) == False
    assert (Action.SCISSOR > Action.PAPER) == True
    assert (Action.SCISSOR > Action.SCISSOR) == False

def test_action_lt():
    """
    Tests overloaded < operator on Action Enum for all possible scenarios 
    """
    assert (Action.ROCK < Action.ROCK) == False
    assert (Action.ROCK < Action.PAPER) == True
    assert (Action.ROCK < Action.SCISSOR) == False
    assert (Action.PAPER < Action.ROCK) == False
    assert (Action.PAPER < Action.PAPER) == False
    assert (Action.PAPER < Action.SCISSOR) == True
    assert (Action.SCISSOR < Action.ROCK) == True
    assert (Action.SCISSOR < Action.PAPER) == False
    assert (Action.SCISSOR < Action.SCISSOR) == False