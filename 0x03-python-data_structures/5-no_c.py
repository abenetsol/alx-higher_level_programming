#!/usr/bin/python3
def no_c(my_string):
    lists = list(my_string)
    for char in lists:
        if char == 'c' or char == 'C':
            lists.remove(char)
    return("".join(lists))
