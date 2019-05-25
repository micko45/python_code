#!/usr/bin/env python
#rounding

#Returns a one or zero for rounding. 
#5 or over returns 1, otherwise 0
answer = []
def round_it_up( divider, remainder ):
  leftover = float(remainder) / float(divider)
  if leftover < 0.5: 
    return 0
  else:
    return 1

count = raw_input("input data:\n")

for i in range(0, int(count)):
  num1, num2 = raw_input().split()
  remain = int(num1) % int(num2)
  answer.append((int(num1) / int(num2)) + round_it_up(num2, remain))

for x in range(len(answer)):
  print answer[x],
