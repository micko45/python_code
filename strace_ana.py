#!/usr/bin/env python
#Do some analsis on strace files. 
from collections import Counter

strace_data = "out.data"

def syscall_total_time(strace_file):
  syscall_all_times = []
  data = open(strace_file)

  for line in data:
    timestamp =  syscall_gettime(line)

    if  timestamp != 0:
      syscall_all_times.append(float(timestamp))

  data.close
  return syscall_all_times

def syscall_gettime(line):
  timestamp = line[line.find('<') + 1:line.find('>')]
  if  timestamp.replace('.','',1).isdigit():
    return timestamp
  else:
    return 0
    
def syscalls_get(strace_in):
  syscalls_array = []
  data = open(strace_in)
  for line in data:
    if '>' in line:
      syscalls_array.append(line[line.find(" "):line.find('(')])
  data.close
  return  syscalls_array

def syscalls_print_array(syscalls_array):
  for i in range(len(syscalls_array)):
    print syscalls_array[i]

def syscalls_count(syscalls_array):
  c = Counter(syscalls_array)
  return c,

def syscalls_unique(syscalls_array):
  syscalls_unique_array = []
  for x in range(len(syscalls_array)):
    if syscalls_array[x] not in syscalls_unique_array:
      syscalls_unique_array.append(syscalls_array[x])

  return syscalls_unique_array

#print out stuff
syscalls_array = syscalls_get(strace_data)
#print syscalls_count(syscalls_array)
#for i in range(len(data)):
#  print data[i]


data = syscall_total_time(strace_data)
print "total: ", sum(data),

unique =  syscalls_unique(syscalls_array)
for x in range(len(unique)):
  print unique[x]

#print "sum of sycalls is : ", sum(syscall_time(strace_data))
