"""
Task 3:
    Write a function that, given two sorted lists, merges them to another sorted list.
    Example:
       #>>> print(merge([2,3,4], [1,5]))
        [1,2,3,4,5]
"""


from auxfuncs import car
from auxfuncs import cdr

__author__ = 'Aurora'


def my_merge_rec(lst_a, lst_b):
    if not lst_a:
        return lst_b
    elif not lst_b:
        return lst_a
    else:
        if car(lst_a) < car(lst_b):
            return car(lst_a).append(my_merge_rec(cdr(lst_a), lst_b))
        else:
            return car(lst_b).append(my_merge_rec(lst_a, cdr(lst_b)))
