#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
Simple calculator that determines the
price of a meal after tax and tip

Author: Alexander A. Laurence
Last modified: January 2019
Website: www.celestial.tokyo
"""

# pricing
meal = 44.5
tax = 6.75/100
tip = 15.0/100

# logic
meal = meal + (meal*tax)
total = meal+(meal*tip)

# print
print(total)