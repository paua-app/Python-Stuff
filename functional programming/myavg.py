"""
Task:
    Write a function that determines the arithmetic average of a given list of numbers.
    Example:
       #>>> print(avg([2,2,4,4]))
        3.0
"""

__author__ = 'Aurora'


def my_avg_imp(lst):
    temp = 0
    for e in lst:
        temp += e
    return float(temp / len(lst))