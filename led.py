#!/usr/bin/env python

from sys import argv
import RPi.GPIO as GPIO ## Import GPIO Library
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) ## Use BOARD pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO pin 7 to OUT
GPIO.setup(11, GPIO.OUT) ## Setup GPIO pin 7 to OUT
GPIO.setup(12, GPIO.OUT) ## Setup GPIO pin 7 to OUT

if argv[1]:
  iterations = argv[1]
  speed = argv[2]
else:
  exit

## Define function named Blink()
def Blink(numTimes, speed):
    for i in range(0,numTimes): ## Run loop numTimes
   #     print "Iteration " + str(i+1) ##Print current loop
        GPIO.output(7, True) ## Turn on GPIO pin 7
        GPIO.output(11, False) ## Turn on GPIO pin 7
        GPIO.output(12, False) ## Turn on GPIO pin 7
        time.sleep(speed) ## Wait
        GPIO.output(7, False) ## Switch off GPIO pin 7
        GPIO.output(11, True) ## Switch off GPIO pin 7
        GPIO.output(12, False) ## Turn on GPIO pin 7
        time.sleep(speed) ## Wait
        GPIO.output(7, False) ## Switch off GPIO pin 7
        GPIO.output(11, False) ## Switch off GPIO pin 7
        GPIO.output(12, True) ## Turn on GPIO pin 7
        if numTimes > 1:
          time.sleep(speed) ## Wait

    print "Done" ## When loop is complete, print "Done"
    GPIO.cleanup()

## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
Blink(int(iterations),float(speed))

