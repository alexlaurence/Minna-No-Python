#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
This app let's you view, add,
update, or delete an event on
the calendar.

Author: Alexander A. Laurence
Last modified: January 2019
Website: www.celestial.tokyo
"""

from time import sleep, strftime

# store user's first name as a string
USER_FIRST_NAME = "Parly"

# create empty dictionary
calendar = {}


# create welcome function
def welcome():
    print("Welcome, " + USER_FIRST_NAME + ".")
    print("Calendar starting...")
    sleep(1)
    print("Today is: " + strftime("%A %B %d, %Y"))
    print("Time is: " + strftime("%H:%M:%S"))
    sleep(1)
    print("What would you like to do?")


# create start function
def start_calendar():
    welcome()
    start = True

    # calendar logic
    while start:
        # prompt user to enter A, U, V, D, or X
        user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")

        # convert to uppercase
        user_choice = user_choice.upper()

        # if user wants to view calendar
        if user_choice == "V":
            # if dictionary has 0 keys
            if len(calendar.keys()) < 1:
                print("Calendar empty.")
            else:
                # print dictionary
                print(calendar)

        # else if the user wants to update calendar
        elif user_choice == "U":
            # ask for the old date
            date = raw_input("What date? ")

            # ask for the new date
            update = raw_input("Enter the update: ")

            # update dictionary
            calendar[date] = update
            print("Calendar updated.")

            # print dictionary
            print(calendar)

        # else if user wants to add to the calendar
        elif user_choice == "A":
            event = raw_input("Enter event: ")
            date = raw_input("Enter date (MM/DD/YYYY): ")

            # check if date contains 10 characters
            # and handle invalid years
            if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
                print("Invalid date was entered.")

                # ask user to try again
                try_again = raw_input("Try Again? (Y/N) ")
                # convert to uppercase
                try_again = try_again.upper()

                # if yes was inputted
                if try_again == "Y":
                    # restart the loop
                    continue
                # if no was inputted
                else:
                    # exit the loop and quit the program
                    start = False
            # Else add valid events to the calendar
            else:
                calendar[date] = event
                print("Successfuly added date!")
                print(calendar)

        # else if user wants to delete to the calendar
        elif user_choice == "D":
            # check if dictionary is empty
            if len(calendar.keys()) < 1:
                print("Calendar is empty.")
            else:
                # prompt user for event
                event = raw_input("What event?")

                # search the dictionary for key
                for date in calendar.keys():
                    # checks for match
                    if event == calendar[date]:
                        # delete the value
                        del calendar[date]
                        print("Successfully deleted!")
                    # else if no match
                    else:
                        print("Incorrect event.")

        # else if user wants to exit app
        elif user_choice == "X":
            # quit the program
            print("Quitting program...")
            start = False
        # else if something else was entered
        else:
            print("Invalid command entered.")

# call the function to start the app
start_calendar()
