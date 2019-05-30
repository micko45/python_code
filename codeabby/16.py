#!/usr/bin/env python
#Average of an array

answer = []
count = raw_input("input data:\n")

#test says we need to round it up if over .5
def rnd_up( divider, remainder ):
  leftover = float(remainder) / float(divider)
  if leftover < 0.5:
    return 0
  else:
    return 1

def get_avg(data):
  avg = total = 0
  for ele in data:
    if int(ele) != 0:
      avg += 1
    total = total + int(ele)
  rmd =  total % avg
  
  return (total / avg) + rnd_up(avg, rmd)

for i in range(0, int(count)):
  data = raw_input().split()
  answer.append(get_avg(data))

for ele in answer:
  print ele,
