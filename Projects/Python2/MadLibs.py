#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
This program generates passages
that are generated in mad-lib format

Author: Alexander A. Laurence
Last modified: January 2019
Website: www.celestial.tokyo
"""

# The template for the story
STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

# user inputs
name = raw_input("Enter a name: ")
adj1 = raw_input("Enter adjective 1: ")
adj2 = raw_input("Enter adjective 2: ")
adj3 = raw_input("Enter adjective 3: ")
verb = raw_input("Enter a verb: ")
noun1 = raw_input("Enter a noun: ")
noun2 = raw_input("Enter another noun: ")
Animal = raw_input("Enter either one of each of the of the following: \n An animal \n A food \n A fruit \n A superhero \n A country \n A dessert \n A year")

# display story
print(STORY) % (name, adj1, adj2, adj3, verb, noun1, noun2, Animal)
