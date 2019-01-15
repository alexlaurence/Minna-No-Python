#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
This app calculates the airplane hanger capacity
for efficient day-to-day running of the airport

Author: Alexander A. Laurence
Last modified: January 2019
Website: www.celestial.tokyo
"""

# number of airplanes in the hanger
airplanes_in_hanger = input("How many airplanes are currently in the hanger? ")
print("Thanks! There are currently %s airplanes in the hanger." % airplanes_in_hanger)

# maximum number of airplanes the hanger can have
max_airplanes_in_hanger = input("How many airplanes can the hanger hold?")
print("Thanks! The hanger can hold up to %s airplanes in the hanger." % max_airplanes_in_hanger)

# define the function to calculate the space in the hanger
def calculate():
    if airplanes_in_hanger >= max_airplanes_in_hanger:
        print("Hanger is full!")
    elif airplanes_in_hanger > (max_airplanes_in_hanger/2):
        print("Hanger is almost full!")
    else:
        print("There's still space in the hanger!")


# call the function
calculate()
