#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
This app plays rock, papers, and scissors
with you!

Author: Alexander A. Laurence
Last modified: January 2019
Website: www.celestial.tokyo
"""

from random import randint

# create list to store the options
options = ["ROCK", "PAPER", "SCISSORS"]

# create a dictionary to print results
message = {
    "tie": "Yawn it's a tie!",
    "won": "Yay you won!",
    "lost": "Aww you lost!"
}

# create function to decide the winner
def decide_winner(user_choice, computer_choice):
    print("You selected: %s."
          % user_choice)
    print("Computer selected: %s."
          % computer_choice)
    if user_choice == computer_choice:
        print(message["tie"])
    # if rock vs scissors
    elif user_choice == options[0] and computer_choice == options[2]:
        print(message["won"])
    # if paper vs rock
    elif user_choice == options[1] and computer_choice == options[0]:
        print(message["won"])
    # if scissors vs paper
    elif user_choice == options[2] and computer_choice == options[1]:
        print(message["won"])
    else:
        print(message["lose"])


# create function to start the game
def play_RPS():
    # user response
    user_choice = raw_input("Enter Rock, Paper, or Scissors: ")

    # set the user input to lowercase
    user_choice = user_choice.upper()

    # check if the incorrect response was made
    if user_choice != "ROCK" and user_choice != "PAPER" and user_choice != "SCISSORS":
        print("Incorrect option.")

        #call the function again
        play_RPS()

    # computer randomly selects either 0, 1, or 2 item in the options list as its choice
    computer_choice = options[randint(0, 2)]

    # call the decide_winner function and pass the above variables as arguments
    decide_winner(user_choice, computer_choice)

    # call the play again function
    play_again()

# create function to restart the game
def play_again():
    # ask user to play again
    ask_restart = raw_input("Play again? (Y/N): ")

    # convert response to upper case
    ask_restart = ask_restart.upper()

    # check response
    if ask_restart == "Y":
        play_RPS()
    elif ask_restart == "N":
        print("Game over!")
    else:
        print("Incorrect entry.")
        play_again()

# call the function to start the game
play_RPS()