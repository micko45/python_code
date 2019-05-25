#!/usr/bin/env python
#less of 3

count = raw_input("data:\n")
answer = []

for i in range(0, int(count)):
  num1, num2, num3  = raw_input().split()
  if int(num1) < int(num2):
    if int(num1) < int(num3):
      answer.append(num1)
    else:
      answer.append(num3)
  else:
    if int(num2) < int(num3):
     answer.append(num2)
    else:
      answer.append(num3)

for x in range(len(answer)):
   print answer[x],
