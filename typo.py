#!/usr/bin/env python
#Typing tourtorial

from random import randint
from sys import exit

correct = 0
incorrect = 0
CODE = [ '(', ')', '[', ']', 
	 '-', '_', '=', '+',
	 '{', '}',

         '1','2', '3', '4', '5', 
	 '6', '7', '8', '9', '0' ]

def results(correct, incorrect):
  print "Result"
  print "---------------"
  print "Right %r" % correct
  print "Wrong %r" % incorrect

while len(CODE) > 1: 
  current_char = CODE[randint(0,len(CODE)-1)]
  print "current Char is %r" % current_char 
  char_input = raw_input('-> ')
  if char_input == current_char:
    print "match"
    correct += 1
  elif char_input == "quit":
    results(correct, incorrect)
    exit()
  else:
    print "no match, yours %r, mine %r" % (char_input, current_char)
    incorrect += 1
