#!/usr/bin/env python

count = raw_input("input data:\n")
answers = []

def get_bmi(w, h):
  return round(float(w) / (float(h) ** 2), 2)

def get_bmi_txt(data):
  if data <= 18.5:
    return "under"
  elif data <= 25.0:
    return "normal"
  elif data <= 30.0:
    return "over"
  else:
    return "obese"

for i in range(0, int(count)):
   weight, hight = raw_input().split()
   data = get_bmi(weight, hight)
   answers.append(get_bmi_txt(data))

print "answer:"

for ele in answers:
  print ele,

