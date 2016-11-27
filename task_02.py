#! usr/bin/env python
# -*- coding: utf-8 -*-

""" continuation of fibonacci task"""

import task_01

def fibo(count):
    """ use a list comprehension to wrap it in a list

    Args:
        count(int) : the total number of fibonacci numbers return

    Retruns:
        fibonacci numbers in order

    Example:
        >>> fibo(5)
        [0, 1, 1, 2, 3]

    """

    fibonacci_number = [i for i in task_01.xfibo(count)]
    return fibonacci_number
