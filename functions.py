# -*- coding: utf-8 -*-
"""
Created on Tue May 17 16:32:40 2022

@author: boloka
"""


def foo(a,b,c=1):
    return a-b+c

def bar(a,b,c):
    return a *b/c
    
def calc_sum(*numbers):
    total = 0
    for number in numbers:
        total  = total + number
        return total

print(calc_sum(1,2,3,9,2))