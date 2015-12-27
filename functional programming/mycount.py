from auxfuncs import car
from auxfuncs import cdr

__author__ = 'Aurora'


def my_count_rek(e, lst):
    if lst == []:
        return 0
    else:
        if car(lst) == [e]:
            return my_count_rek(e, cdr(lst)) + 1
        else:
            return my_count_rek(e, cdr(lst)) + 0

def my_count_er(e, lst):
    return None