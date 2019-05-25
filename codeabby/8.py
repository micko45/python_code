#!/usr/bin/env python
#Arithmetic progression

count = raw_input("data:\n")
answer = []
#Work out the sum of an progresion
def work_out_progression(val, step, times):
  tmp = total = int(val)
  for x in range(1, int(times)): 
    tmp = int(tmp) + int(step)
    total = total + tmp
  return total
  
for i in range(0, int(count)):
  val, step, times = raw_input().split()
  answer.append(work_out_progression(val, step, times))

print "\nanswer:"

for y in range(len(answer)):
  print answer[y],
