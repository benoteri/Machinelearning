# -*- coding: utf-8 -*-
"""
Created on Thu May 19 16:51:19 2022
Arithmetic module
@author: boloka
"""

def add (a,b):
    return a + b

def minus (a,b):
    return a-b
def mult(a,b):
    return a * b
def divide(a, b):
    return a/b
def main():
    x = 16
    y = 8
    print(add(x,y))
    print(minus(x, y))
    print(mult(x,y))
    print(divide(x,y))
    
if __name__== '__main__':
    
    main()
