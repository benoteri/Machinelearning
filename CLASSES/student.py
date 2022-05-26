# -*- coding: utf-8 -*-
"""
Created on Thu May 26 16:26:40 2022

@author: boloka
"""
from person import Person
class Student(Person):
    
    def __init__(self,first, last, ID, school,major):
        super().__init__(first,last,ID)
        self._school = school
        self._major = major
        
    def get_school(self):
        return self._school
    def get_major(self):
        return self._major
    def get_name(self):
        return super().get_last()+ ", "+ \
            super().get_first()
            
    def __str__(self):
        return "Name: " + self._first + self._last +  "\nID: " + str(self._ID)