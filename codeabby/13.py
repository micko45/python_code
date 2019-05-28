#!/usr/bin/env python
#weigheted sum of digits. 

raw_input("input data:\n")

def  weighted(data):
  answer = []
  for ele in data:
    total = 0
    for x in range(0, len(ele)):
      total = int(ele[x])*(x+1) + total
    answer.append(total)
  return answer
  
data = raw_input().split()
print "answer:"
answer = weighted(data)

for ele in answer:
  print ele, 
