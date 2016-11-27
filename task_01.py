#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" fibonacci synthesizing tasks"""


def xfibo(count):
    """ a generator that will yield each number in a fibonacci sequence

    Args:
        count (int) the number of fibonacci numbers to return

    Retturns:
        fibonacci numbers in order

    Examples:
        >>> for i in xfibot(5):
            print i
        ...
        0
        1
        1
        2
        3
        """
    iteration = 0
    lastnumber, currentnumber = 0, 1
    while iteraction < count:
        yield lastnumber
        num2, num1 = lastnumber, currentnumber + lastnumber
        iteraction +=1
        
