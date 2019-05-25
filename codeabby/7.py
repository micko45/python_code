#!/usr/bin/env python
# Fahrenheit to Celsius

data = raw_input("data:\n").split()

def round_it_up( divider, remainder ):
  leftover = float(remainder) / float(divider)
#  print remainder / divider
  if leftover < 0.5:
    return 0
  else:
    return 1

for i in range(1, int(data[0])+1):
  num1 = int(data[i]) -32
  remain =  num1 % 1.8
  fahr = int((num1 / 1.8) + round_it_up(num1, remain))
  #fahr = int((int(data[i]) -32) / 1.8)
  print fahr,
