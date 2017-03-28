#use argv from sys

prompt = "-> "
print "how much cheese"
cheese = int(raw_input(prompt))
print "how much crackers"
crackers = int(raw_input(prompt))

def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print "you have %d cheeses!" % cheese_count
  print "you have %d boxes of crackers!!" % boxes_of_crackers
  print "Man thats enough for a party"

cheese_and_crackers(cheese, crackers)
