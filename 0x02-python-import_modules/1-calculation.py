#!/usr/bin/python3
from calculator_1 import *
a = 10
b = 5
sums = add(a, b)
subt = sub(a, b)
mults = mul(a, b)
divs = div(a, b)
print("{:d} + {:d} = {:d}".format(a, b, sums))
print("{:d} - {:d} = {:d}".format(a, b, subt))
print("{:d} * {:d} = {:d}".format(a, b, mults))
print("{:d} / {:d} = {:d}".format(a, b, divs)) 
