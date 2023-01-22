import random
import logging
from action import Action
from exception.exception import InvalidChoiceError

logging.basicConfig(filename='/logs/game.log', level=logging.INFO)

class RockPaperScissors:
    """
    A class representing the Rock-Paper-Scissors game. 
    It has the following properties:
    - action: a list of the Action enumeration options (rock, paper, scissors)
    - wins: an integer representing the number of wins the player has
    - losses: an integer representing the number of losses the player has
    - ties: an integer representing the number of ties the player has

    It has the following methods:
    - get_user_action(): prompts the user to enter a choice (rock, paper, or scissors) and returns the corresponding Action enumeration.
    - get_computer_action(): randomly selects an action from the self.action list and returns it.
    - determine_winner(user_action: Action, computer_action: Action): takes in the user's action and the computer's action and compares them.
    - print_score(): prints the player's current score (number of wins, losses, and ties).
    - play_round(): plays a round of the game.
    - player_wants_to_play_again(): prompts the user to enter whether they want to play again and returns a boolean value indicating their choice.
    - run_game(): runs the game by calling the play_round() and player_wants_to_play_again() methods in a loop until the player decides to stop playing.
    """


    def __init__(self):
        """ Initializes the properties of the class"""
        self.action = [Action.Rock, Action.Paper, Action.Scissors]
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def get_user_action(self) -> Action:
        """
        Prompts the user to enter a choice (rock, paper, or scissors) and returns the corresponding Action enumeration.
        Raises an InvalidChoiceError if the user enters an invalid choice.
        """
        try:
            user_input = int(input("Enter a choice:\n1 for rock\n2 for paper\n3 for scissors"))
            if user_input not in [1,2,3]:
                raise InvalidChoiceError(user_input)
            
            action = Action(user_input)
            return action
        except InvalidChoiceError as ic:
            raise InvalidChoiceError("Invalid Input", ic.args)

    def get_computer_action(self) -> Action:
        """ Randomly selects an action from the self.action list and returns it."""
        computer_action = random.choice(self.action)
        return computer_action


    def determine_winner(self, user_action: Action, computer_action: Action):
        """
        Compares the user's action and the computer's action and prints the result of the round.
        Updates the self.wins,self.losses, and self.ties properties accordingly.
        """
        if user_action == computer_action:
            print(f"Both players selected {user_action.name}. It's a tie!")
            self.ties += 1
        elif user_action == Action.Rock:
            if computer_action == Action.Scissors:
                print("Rock smashes scissors! You win!")
                self.wins += 1
            else:
                print("Paper covers rock! You lose.")
                self.losses += 1
        elif user_action == Action.Paper:
            if computer_action == Action.Rock:
                print("Paper covers rock! You win!")
                self.wins += 1
            else:
                print("Scissors cuts paper! You lose.")
                self.losses += 1
        elif user_action == Action.Scissors:
            if computer_action == Action.Paper:
                print("Scissors cuts paper! You win!")
                self.wins += 1
            else:
                print("Rock smashes scissors! You lose.")
                self.losses += 1

    
    def print_score(self):
        """ Prints the player's current score (number of wins, losses, and ties)."""
        print(f"You have {self.wins} wins, {self.losses} losses, and {self.ties} ties.")


    def play_round(self):
        """ Plays a round of the game."""
        try:
            user_action = self.get_user_action()
            computer_action = self.get_computer_action()
            print(f"\nYou picked {user_action.name}, and I picked {computer_action.name}.")
            self.determine_winner(user_action, computer_action)
            self.print_score()
        except Exception as ex:
            print("Please Enter either 1, 2 or 3", ex.args)
        

    def player_wants_to_play_again(self) -> bool:
        """ 
        Prompts the user to enter whether they want to play again and returns a boolean value indicating their choice.
        If user enters invalid input prompts user again
         """
        prompt = "\nDo you wish to play again? (y/n): "
        valid_choices = ("y", "n")
        while True:
            user_choice = input(prompt).strip().lower()
            if user_choice in valid_choices:
                return user_choice == "y"

            print("Invalid input!") 

    def run_game(self):
        """ Runs the game by calling the play_round() and player_wants_to_play_again() methods in a loop until the player decides to stop playing."""
        while True:   
            self.play_round()
            if not self.player_wants_to_play_again():
                print("Thank you for playing the game")
                break
            
            