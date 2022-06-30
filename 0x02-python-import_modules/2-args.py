#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv)
    i = 2
    print("{:d} arguments:".format(count-1))
    while i <= count:
        print("{:d}: {:s}".format(i-1, argv[i - 1]))
        i+=1
          
