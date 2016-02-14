"""
Task:
    Write a function that returns two lists. One should contain all even numbers and one all odd numbers from the input.
    Example:
       #>>> print(split([1,2,3,4,5,6]))
        [[2,4,6], [1,3,5]]
"""

__author__ = 'Aurora'

from auxfuncs import car
from auxfuncs import cdr


def my_split_imp(lst):
    lout = []
    rout = []
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            lout.append(lst[i])
        else:
            rout.append(lst[i])
        i += 1
    return [lout, rout]


def my_split_tr(lst, out1=[], out2=[]):
    if not lst:
        return list(out1,out2)
    else:
        if car(lst) % 2 == 0:
            out1.append(car(lst))
        else:
            out2.append(car(lst))
        my_split_tr(cdr(lst), out1, out2)


def my_split_hof(lst):
    return list(list(filter(lambda x: x % 2 == 0), lst),
                list(filter(lambda x: x % 2 == 1), lst))