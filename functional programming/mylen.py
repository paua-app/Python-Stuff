"""
Task:
    Write a function that calculates the length of a list.
    Example:
       #>>> print(len([1,2,3,4,5]))
        5
"""

from auxfuncs import cdr
from auxfuncs import build_list as bl

__author__ = 'Aurora'


def my_len_rec(lst):
    """
    Recursive approach
    :rtype: integer
    :param lst: a list of elements which length is to be determined
    :return: the length of lst
    """
    if not lst:
        return 0
    else:
        return 1 + my_len_rec(cdr(lst))


def my_len_tr(lst, acc=0):
    """
    Tail-Recursive approach.
    Features a counter for the list length, which is returned when the list is iterated over completely
    Default value 0 as neutral element for addition.
    :rtype: integer
    :param lst: List of which the length is required
    :param acc: counter for the length. Should be left blank at function call.
    :return: the length of lst
    """
    if not lst:
        return acc
    else:
        return my_len_tr(cdr(lst), acc+1)


def my_len_hof(f, lst):
    """
    Approach using Higher-Order Functions
    :rtype : integer
    :param f: the function to be applied in order to determine the length of lst
    :param lst: a list of elements which length is to be determined
    :return: the length of lst
    """
    return False


def my_len_test():
    """
    Test for all three functions
    :rtype: string
    :return: the test message and a return value of all three main functions (which should be equal)
    """
    length = 10
    lst = bl(length)
    return ("Determining the length of {0}.\n"
            "\tShould be: {1}\n"
            "\tRecursive approach: {2}\n"
            "\tTail-Recursive approach: {3}\n"
            "\tHOF-approach: {4}".format(lst,
                                         length,
                                         my_len_rec(lst),
                                         my_len_tr(lst),
                                         my_len_hof(None, lst)))
