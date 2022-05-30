# -*- coding: utf-8 -*-
"""
Created on Mon May 30 17:47:49 2022

@author: HENRY
"""

from person import Person
class Lecturer(Person):
    def __init__(self,title,first,last,ID,course):
        super().__init__(first,last,ID)
        self._title = title
        self._course = course
    
    def get_title(self):
        return self._title
    
    #set methods
    def set_course(self, x):
        self._course = x
   #get methods 
    def get_course(self):
        return self._course
    
    
    def get_name(self):
        return self._title + " "+ super().get_first() +", "+ super().get_last()
    
    def __str__(self):
        return "Name: "+ self._title + self._first + self._last +\
            "\nCourse: "+ self._course
              
            