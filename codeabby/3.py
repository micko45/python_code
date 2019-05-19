#!/usr/bin/env python 
#Sums in Loop

count = raw_input("data:\n")
answers = []

for i in range(0, int(count)) :
   num1, num2 = raw_input().split()
   answers.append(int(num1) + int(num2))

for x in range(len(answers)):
  print answers[x],
