import logging
from activity.RockPaperScissor import RockPaperScissor
from agent.HumanPlayer import HumanPlayer
from agent.ComputerPlayer import ComputerPlayer
from result.Result import Result
from activity.Action import Action


logging.basicConfig(filename='log/game.log', level=logging.INFO)
logger = logging.getLogger('rock-paper-scissors-logger')


def print_score(human_player):
    """ 
    Prints the player's current score (number of wins, losses, and total number of games).
    
    Parameters:
        human_player (HumanPlayer): Object of the HumanPlayer class representing the user.
    """
    logging.info(f"Games won = {human_player.game_win}, Games lost = {human_player.game_lose}")
    print(f"You have played {human_player.game_count} games, out of which you won {human_player.game_win} and lost {human_player.game_lose}.")


def process_result_tie(player1, player2, action1, action2):
    """ 
    Updates game_count property of both the players in the case of tie
    
    Parameters:
        player1 (HumanPlayer): Object of the HumanPlayer class capturing behaviour of the user.
        player2 (ComputerPlayer): Object of the ComputerPlayer class capturing behaviour of the Computer.
        action1 (Action): User's selected Action
        action2 (Action): Computer's selected Action
    """
    player1.game_count += 1
    player2.game_count += 1
    logging.info(f"Game Count = {player1.game_count}, Player 1 Action = {action1},\
    Player 2 Action = {action2}, Result = {Result.TIE.name}")
    print(f"It's a tie!")


def process_result_win(player1, player2, action1, action2):
    """ 
    Updates game_count, game_win, game_lose property of the players in the case of win
    
    Parameters:
        player1 (HumanPlayer): Object of the HumanPlayer class capturing behaviour of the user.
        player2 (ComputerPlayer): Object of the ComputerPlayer class capturing behaviour of the Computer.
        action1 (Action): User's selected Action
        action2 (Action): Computer's selected Action
    """
    player1.game_count += 1
    player2.game_count += 1
    player1.game_win += 1
    player2.game_lose += 1
    logging.info(f"Game Count = {player1.game_count}, Player 1 Action = {action1},\
    Player 2 Action = {action2}, Result = {Result.WIN.name}")
    print(f"You win")


def process_result_lose(player1, player2, action1, action2):
    """ 
    Updates game_count, game_win, game_lose property of the players in the case of loss
    
    Parameters:
        player1 (HumanPlayer): Object of the HumanPlayer class capturing behaviour of the user.
        player2 (ComputerPlayer): Object of the ComputerPlayer class capturing behaviour of the Computer.
        action1 (Action): User's selected Action
        action2 (Action): Computer's selected Action
    """
    player1.game_count += 1
    player2.game_count += 1
    player1.game_lose += 1
    player2.game_win += 1
    logging.info(f"Game Count = {player1.game_count}, Player 1 Action = {action1},\
    Player 2 Action = {action2}, Result = {Result.LOSE.name}")
    print(f"You Lose")


def play_round(player1, player2):
    """ 
    Plays a round of the game.
    
    Parameters:
        player1 (HumanPlayer): Object of the HumanPlayer class capturing behaviour of the user.
        player2 (ComputerPlayer): Object of the ComputerPlayer class capturing behaviour of the Computer.
    """
    try:
        choices = [f"{action.name}[{action.value}]" for action in Action]
        choices_str = "Enter your choice : " + ", ".join(choices)
        print(choices_str)
        action1 = player1.action
        action2 = player2.action
        print(f"\nYou picked {action1.name}, and Computer picked {action2.name}.")
        result = RockPaperScissor.determine_winner(action1, action2)
        
        if(result == Result.TIE):
            process_result_tie(player1, player2, action1, action2)
        elif(result == Result.WIN):
            process_result_win(player1, player2, action1, action2)
        elif(result == Result.LOSE):
            process_result_lose(player1, player2, action1, action2)

    except Exception as ex:
        logger.error(f"Exception Occured. {ex.args[0]}")
        print("Please Enter either 0, 1 or 2.", ex.args[0])
    

def is_play_again() -> bool:
    """ 
    Prompts the user to enter whether they want to play again and 
    returns a boolean value indicating their choice.
    If user enters invalid input prompts user again
    """
    prompt = "\nDo you wish to play again? (y/n): "
    valid_choices = ("y", "n")
    while True:
        user_choice = input(prompt).strip().lower()
        if user_choice in valid_choices:
            return user_choice == "y"

        logger.warning(f"Invalid Input {user_choice}")
        print("Invalid input! Please enter either y or n")


def run_game():
    """ Runs the game by calling the play_round() and is_play_again() methods
    in a loop until the player decides to stop playing.
    """
    human_player = HumanPlayer()
    computer_player = ComputerPlayer()
    logger.info("Game Starts")
    while True:   
        play_round(human_player, computer_player)
        if not is_play_again():
            print("Thank you for playing the game")
            print_score(human_player)
            logger.info("Game Ends")
            break
    

if __name__ == "__main__":
    """
    Main function to run the game
    """
    try:
        run_game()
    except Exception as ex:
        logging.critical("Unhandled Exception Occured", exc_info=True)
        print("Application is currently down. Please check back after sometime")