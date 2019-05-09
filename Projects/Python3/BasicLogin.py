#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

"""
This is a very basic login system
which logs the user in if the username
and password correctly matches the data
stored on the dictionary.

Author: Alexander A. Laurence
Last modified: May 2019
Website: www.celestial.tokyo
"""

import getpass 

# Instantiate The Dictionary
password_index = {
     1 : {'Username': 'mrbooleanswag','Password': '1234'},
     2 : {'Username': 'Lexington','Password': 'kfsdjgfdg'}
}

# Get User input
get_username = input('Username: ')
get_password = getpass.getpass('Password: ')

# Set bools to false
auth_username = False
auth_password = False

# Search Dictionary
i = 1
while i < len(password_index) + 1:
  if password_index[i]['Username'] == get_username:
    auth_username = True
    
    j = 1
    while j < len(password_index) + 1:
      if password_index[j]['Password'] == get_password:
        auth_password = True
        break
      j += 1
    break
  i += 1
  
# Authentication Logic
if auth_username == False:
  print('Incorrect username.')
  
if auth_password == False:
  print('Incorrect Password')
  
if auth_password == False or auth_username == False:
  print('Failed to log in')
  
if auth_password == True and auth_username == True:
  print('Successfully logged in')
