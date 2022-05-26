# -*- coding: utf-8 -*-
"""
Created on Thu May 26 15:39:58 2022

@author: boloka
"""
class Person:
    
    count = 0
    
    def __init__(self,first,last,ID):
       #for creating new objects 
        self._first = first 
        self._last = last
        self._ID = ID
        self.__class__.count +=1
        
    def get_count(self):
        return self.__class__.count
    
    def set_first(self, first):
        self._first= first + " " + self._last
        
    def set_last(self,last):
        self._last = last
        
    def set_ID(self,ID):
        self._ID = ID
    
    def get_first(self):
        return self._first
    
    def get_last(self):
        return self._last
    
    def get_ID(self):
        return self._ID
    
    def __str__(self):
        return self_first + " " + self._last
    
    