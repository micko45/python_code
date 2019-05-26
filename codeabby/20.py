#!/usr/bin/env python
#Vowel Count

vowels = { 'a', 'e', 'i', 'o', 'u', 'y' }
count = raw_input("input data:\n")
answer = []

def check(x):
  total = 0
  for ele in x:
    for ele1 in vowels:
      if ele == ele1:
        total += 1
  return total
  

for i in range(0, int(count)):
  data = raw_input()
  answer.append(check(data)) 

print "\nanswer: "
for ans in answer:
  print ans,
