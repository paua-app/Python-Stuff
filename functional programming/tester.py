"""
Tests all tasks.
"""

from mylen import my_len_test as lt
from mycount import my_count_test as ct

__author__ = 'Aurora'

def pwb(str):
    """
    prints a given string with an additional line break at the end
    :param str: stringt to print
    :return: None
    """
    print(str + "\n")

pwb("This is a complete test run of all functions.\n"
    "Each test should state the task and print out the result of it's three functions.\n"
    "The 'should be' value should be determined with a built-in function or a constant used at test setup.\n")
pwb(lt())
pwb(ct())
