from auxfuncs import cdr

__author__ = 'Aurora'


def my_len_rek(lst):
    if lst == []:
        return 0
    else:
        return 1 + my_len_rek(cdr(lst))
