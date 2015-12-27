__author__ = 'Aurora'

def car(lst):
    return lst[:1]

def first(lst):
    return car(lst)

def head(lst):
    return car(lst)

def cdr(lst):
    return lst[1:]

def rest(lst):
    return cdr(lst)

def tail(lst):
    return(cdr(lst))

def last(lst):
    """
    Given a list of objects, returns the last element from the list
    :param lst:
    :return:
    """
    return lst[len(lst)-1]

a = [1,2,3,4]
print(car(a) == [1])