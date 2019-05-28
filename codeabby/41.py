#!/usr/bin/env python
#Median of Three

count = raw_input("data:\n")
answer = []

def return_median(x):
  a, b, c = int(x[0]), int(x[1]), int(x[2])

  if a > b and a < c or a < b and a > c:
    return a

  elif b > c and b < a or b < c and b > a:
    return b
    
  else: 
    return c

for x in range(0, int(count)):
  data = raw_input().split()
  answer.append(return_median(data))

print "answer:"
for ele in answer:
  print ele,
