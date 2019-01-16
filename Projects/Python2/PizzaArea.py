#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
This app calculates the area of circles and triangles

Author: Alexander A. Laurence
Last modified: January 2019
Website: www.celestial.tokyo
"""
print("Pizza Area Calculator is running...")
option = raw_input("What do you want to calculate? Enter 'whole' for the whole pizza or 'piece' for one piece: ")
option = option.lower()

if option == 'whole':
    radius = float(raw_input("Enter the radius: "))
    area = 3.14159 * radius ** 2
    print("Area of Pizza with radius (%s) is: %s" % (radius, area))

elif option == 'piece':
    base = float(raw_input("Enter the base: "))
    height = float(raw_input("Enter the height: "))
    area = 0.5 * base * height
    print("Area of the piece with base (%s) and height (%s) is: %s" % (base, height, area))

else:
    print("%s is an invalid input" % (option))

print("Pizza Area Calculator is stopping...")
