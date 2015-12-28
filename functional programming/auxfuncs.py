"""
A collection of auxiliary functions, i.e. some list access and higher-order functions and generators.
NOT necessarily compliant with functional programming standards
"""

from random import randrange as rr

__author__ = 'Aurora'


def car(lst):
    """
    Returns the first element (head) of the given list, if it is not empty, else False
    :param lst: the list to be decapitated
    :return: the first element of lst
    """
    return lst[:1]


def first(lst):
    return car(lst)


def head(lst):
    return car(lst)


def cdr(lst):
    """
    Returns the tail of the given list, meaning the entire list without the first element (head)
    :param lst:
    :return: tail of lst
    """
    return lst[1:]


def rest(lst):
    return cdr(lst)


def tail(lst):
    return cdr(lst)


def last(lst):
    """
    Given a list of objects, returns the last element from the list, if it is not empty, else False
    :param lst: the list of which the last element should be returned
    :return: the last element of lst
    """
    # noinspection PyBroadException
    try:
        if not lst:
            return False
        return lst[len(lst) - 1]
    except:
        print("Error: Not a list!")
        return False


def build_list(length):
    """
    builds a list of integers of length length
    :param length: length of the list-to-build
    :return: a list of length length
    """
    return build_list_with_step(length, 1)


def build_list_with_step(length, step):
    """
    builds a list of integers of length length with an interval of size step between each two elements.
    :param length: length of the output list
    :param step: interval between two following elements
    :return: a list of up to length elements with an interval of step
    """
    lst = []
    i = 0
    while len(lst) < length:
        if i % step == 0:
            lst.append(i)
        i += 1
    return lst


def build_random_list(length, interval_start_value, interval_end_value):
    """
    Creates a list with random integer elements within a certain interval
    :param length: integer: length of the output list
    :param interval_start_value: start value of the output list interval
    :param interval_end_value: end value of the output list interval
    :return: a list with random integers within the given interval
    """
    return build_random_list_steps(length, interval_start_value, interval_end_value, 1)


def build_random_list_steps(length, interval_start_value, interval_end_value, step):
    """
    Creates a list with random integer elements within a certain interval
    :param length: integer: length of the output list
    :param interval_start_value: start value of the output list interval
    :param interval_end_value: end value of the output list interval
    :param: step: the smallest possible difference between two elements
    :return: a list with random integers within the given interval
    """
    lst = []
    while len(lst) < length:
        lst.append(rr(interval_start_value, interval_end_value, step))
    return lst
