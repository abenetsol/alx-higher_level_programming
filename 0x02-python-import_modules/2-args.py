#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv)
    i = 2
    print("{:d} {:s}{:s}".format(count-1, "argument" if count <=2 else "arguments", 
                                 "." if count == 1 else ":"))
    while i <= count:
        print("{:d}: {:s}".format(i-1, argv[i - 1]))
        i+=1
          
