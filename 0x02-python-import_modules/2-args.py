#!/usr/bin/python3
import sys
count = len(sys.argv)
i = 2
print("{:d} arguments:".format(count-1))
while i <= count:
    print("{:d}: {:s}".format(i-1, sys.argv[i - 1]))
    i+=1
          
