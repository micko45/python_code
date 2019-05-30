#!/usr/bin/env python
#Array checksum

count = raw_input("input data:\n")

def checksum(toget):
  result = 0
  limit = 10000007 
  for ele in toget:
    result = (result+ele)*113 
  print result % limit

checksum(map(int, raw_input().split()))
