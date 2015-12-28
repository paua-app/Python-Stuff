from auxfuncs import car
from auxfuncs import cdr
from auxfuncs import build_random_list as brl

__author__ = 'Aurora'


def my_count_rec(e, lst):
    if lst == []:
        return 0
    else:
        if car(lst) == [e]:
            return my_count_rec(e, cdr(lst)) + 1
        else:
            return my_count_rec(e, cdr(lst)) + 0  #


def my_count_tr(e, lst):
    return None

def my_count_hof(e, lst):
    return None

def my_count_test():
    """
    Test for all three functions
    :rtype: string
    :return: the test message and a return value of all three main functions (which should be equal)
    """
    ele = 1
    lst = brl(10, 0, 3)
    return("Determining the length of {0}.\n"
          "\tShould be: {1}\n"
          "\tRecursive approach: {2}\n"
          "\tTail-Recursive approach: {3}\n"
          "\tHOF-approach: {4}".format(lst,
                                     lst.count(ele),
                                     my_count_rec(ele, lst),
                                     my_count_tr(ele, lst),
                                     my_count_hof(ele, lst)))