#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv)
    print("{:d} {:s}{:s}".format(count - 1, "argument" if count <= 2 else "arguments", 
                                 "." if count == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
