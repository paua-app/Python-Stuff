from auxfuncs import car
from auxfuncs import cdr
from auxfuncs import build_random_list as brl

__author__ = 'Aurora'


def my_count_rec(e, lst):
    if not lst:
        return 0
    else:
        if car(lst) == [e]:
            return my_count_rec(e, cdr(lst)) + 1
        else:
            return my_count_rec(e, cdr(lst)) + 0


def my_count_tr(e, lst, acc=0):
    if not lst:
        return acc
    else:
        if car(lst) == [e]:
            return my_count_tr(e, cdr(lst), acc + 1)
        else:
            return my_count_tr(e, cdr(lst), acc)


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
    return ("Determining occurrences of '{0}' in {1}:.\n"
            "\tshould be: {2}\n"
            "\tRecursive approach: {3}\n"
            "\tTail-Recursive approach: {4}\n"
            "\tHOF-approach: {5}".format(ele,
                                         lst,
                                         lst.count(ele),
                                         my_count_rec(ele, lst),
                                         my_count_tr(ele, lst),
                                         my_count_hof(ele, lst)))
