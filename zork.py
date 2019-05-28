#!/usr/bin/env python
#zork 27/5/2019

import sys
import time
import random

def ps( str ):
#def print_text_slow( str ):
  for letter in str:
    sys.stdout.write(letter) 
    sys.stdout.flush() 
    time.sleep(.01)
    #time.sleep(.1)

  sys.stdout.write(" ") 
  sys.stdout.flush() 

def front_door():
  ps("There is a door in front of you.")
  ps("What will you do\n")


def welcome_to_zork():
  ps("Welcome stranger, to the land of Zork\n")
  ps("What is you name?\n")
  name = raw_input()
  
  ps("Welcome " + name +"\n")
  ps("So " + name + " What would you like to do?\nChoose:")
  data = raw_input()  
  if data == "look":
    ps("you look around, all is as it should be\n")
    ps("THE END\n")
  else:
    ps("you die\n")

welcome_to_zork()
