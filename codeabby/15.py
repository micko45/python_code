#!/usr/bin/env python
#Max/Min of array

data = raw_input("input data: \n").split()

def get_big(x):
  compair = 0
  for ele in x:
    if int(ele) > compair:
      compair = int(ele)

  return compair

def get_small(x):
  compair = x[0]
  for ele in x:
    if int(ele) < compair:
      compair = int(ele)

  return compair

print "answer:\n", get_big(data), get_small(data)
