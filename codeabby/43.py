#!/usr/bin/env python
#Dice rolling

count = raw_input("input data:\n")
answer = []

def roll_dice(data):
  #print data
  return int((float(data)*6)+1)

for i in range(0, int(count)):
  data = raw_input()#.split
  answer.append(roll_dice(data))

for ele in answer:
  print ele,
