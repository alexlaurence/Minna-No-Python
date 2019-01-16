#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
a program that rolls a pair of dice
and asks the user to guess the sum.
If the user's guess is equal to the
total value of the dice roll, the
user wins! Otherwise, the computer wins.

Author: Alexander A. Laurence
Last modified: January 2019
Website: www.celestial.tokyo
"""

from random import randint
from time import sleep

def get_user_guess():
    guess = int(raw_input("Guess a number: "))
    return guess

def roll_dice(number_of_sides):
    # roll the dice
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)

    # maximum possible value
    max_val = number_of_sides * 2
    print("The maximum possible value is: %d" % max_val)

    # return the user's guess
    guess = get_user_guess()

    # check invalid input
    if guess > max_val:
        print("No guessing higher than the maximum possible value!")
    # game logic
    else:
        print("Rolling...")
        sleep(1)
        print("The first dice is %s" % first_roll)
        sleep(1)
        print("The second dice is %s" % second_roll)
        sleep(1)
        total_roll = first_roll + second_roll
        print("The total roll is %s" % total_roll)
        print("Result...")
        sleep(1)

        if guess > total_roll:
            print ("You won!")
        else:
            print ("You Lose!")

# call the function to start game, 
# pass value 6 for number_of_sides
roll_dice(6)