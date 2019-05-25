#!/usr/bin/env python
#Do some analsis on strace files. 
from collections import Counter

#Strace file must be created with options "strace -ttT -o out.data"
strace_data = "out.data"

#Get time into array for all calls
def syscall_total_time(strace_file):
  syscall_all_times = []
  data = open(strace_file)

  for line in data:
    timestamp =  syscall_gettime(line)

    if  timestamp != 0:
      syscall_all_times.append(float(timestamp))

  data.close
  return syscall_all_times

#get time of calls and return them
def syscall_gettime(line):
  timestamp = line[line.find('<') + 1:line.find('>')]
  if  timestamp.replace('.','',1).isdigit():
    return timestamp
  else:
    return 0
    
#get all calls and return them in an array
def syscalls_get(strace_in):
  syscalls_array = []
  data = open(strace_in)
  for line in data:
    if '>' in line:
      syscalls_array.append(line[line.find(" "):line.find('(')])
  data.close
  return  syscalls_array

#Get all uniquie calls, return array
def syscalls_unique(syscalls_array):
  syscalls_unique_array = []
  for x in range(len(syscalls_array)):
    if syscalls_array[x] not in syscalls_unique_array:
      syscalls_unique_array.append(syscalls_array[x])

  return syscalls_unique_array

#print out an array of calls
def syscalls_print_array(syscalls_array):
  for i in range(len(syscalls_array)):
    print syscalls_array[i]

#count amount of calls, return hash table
def syscalls_count(syscalls_array):
  c = Counter(syscalls_array)

  return c

#Work out total time per systemcall
def syscall_uniquie_time(syscall, strace_file):
  data = open(strace_file)
  total = float()

  for line in data:
    if syscall in line:
      total = total + float(syscall_gettime(line))
  return total

#print out stuff
#for i in range(len(data)):
#  print data[i]

#data = syscall_total_time(strace_data)
#print "total: ", sum(data),

#for x in range(len(unique)):
#  print unique[x]
#print "sum of sycalls is : ", sum(syscall_total_time(strace_data))
###################################################
##########main#####################################
###################################################

syscalls_array = syscalls_get(strace_data)
unique =  syscalls_unique(syscalls_array)
syscall_to_check = "newfstatat"
c = syscalls_count(syscalls_array)
#print type(c)
#print list(c)
for ele in  c:
  print ele,c[ele]


#print "total time in call :", syscall_to_check, syscall_uniquie_time(syscall_to_check, strace_data)
def print_unique_time():
  for i in range(len(unique)):
    print "total time in call :", unique[i], syscall_uniquie_time(unique[i], strace_data)

#print_unique_time()

