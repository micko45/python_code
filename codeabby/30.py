#!/usr/bin/env python
#Reverse String

string = raw_input("input data:\n")
count = len(string) -1 
toPrint = str()

for i in string:
  toPrint = toPrint + str(string[count])
  count -= 1

print toPrint
