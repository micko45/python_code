#!/usr/bin/env python
#min-of-two

count = raw_input("data:\n")
answer = []

for i in range(0, int(count)): 
  num1, num2 = raw_input().split()
  if int(num1) < int(num2):
    answer.append(num1)
  else:
     answer.append(num2)

for x in range(len(answer)):
   print answer[x],
