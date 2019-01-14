#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
This app calculates the accuracy of shots on goal in football

Author: Alexander A. Laurence
Last modified: January 2019
Website: www.celestial.tokyo
"""

# number of shots that didn't hit the goal
shots_offTarget = input("How many shots did not hit the target? ")
print("Ok, so %s shots failed to the target." % shots_offTarget)

# number of shots that hit the goal
shots_onTarget = input("How many shots hit the target? ")
print("Ok, so %s shots hit the target." % shots_offTarget)

# the percentage accuracy
shot_accuracy = shots_onTarget / (shots_onTarget + shots_offTarget)*100
print("That means your shot accuracy was %s." % shot_accuracy)
