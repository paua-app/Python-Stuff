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
    try:
        if lst == []:
            return 0
        else:
            return 1 + my_len_rec(cdr(lst))
    except TypeError:
        return "Error! Incompatible Types in Function: mylen::my_len_rec"
    except ValueError:
        return "Error! Bad value in Function: mylen::my_len_rec"
    except:
        return "Error! Unknown Exception in Function mylen::my_len_rec"


def my_len_tr(lst):
    """
    Tail-Recursive approach (init).
    :rtype: integer
    :param lst: a list of elements which length is to be determined
    :return: the length of lst
    """
    my_len_tr_aux(lst, 0)


def my_len_tr_aux(lst, acc):
    """
    Auxiliary function for Tail-Recursive approach.
    Features a counter for the list length, which is returned when the list is iterated over completely
    :rtype: integer
    :param lst: List of which the length is required
    :param acc: counter for the length
    :return: the length of lst
    """
    try:
        if lst == []:
            return acc
        else:
            acc += 1
            return my_len_tr_aux(cdr(lst), acc)
    except TypeError:
        return "Error! Incompatible Types in Function: mylen::my_len_tr"
    except ValueError:
        return "Error! Bad value in Function: mylen::my_len_tr"
    except:
        return "Error! Unknown Exception in Function mylen::my_len_tr"


def my_len_hof(lst):
    """
    Approach using Higher-Order Functions
    :rtype : integer
    :param lst: a list of elements which length is to be determined
    :return: the length of lst
    """
    return False


def my_len_test():
    """
    Test for all three functions
    :rtype: string
    :return: None
    """
    length = 10
    lst = bl(length)
    return("Determining the length of {0}.\n"
          "\tShould be: {1}\n"
          "\tRecursive approach: {2}\n"
          "\tTail-Recursive approach: {3}\n"
          "\tHOF-approach: {4}".format(lst,
                                     length,
                                     my_len_rec(lst),
                                     my_len_tr(lst),
                                     my_len_hof(lst)))
