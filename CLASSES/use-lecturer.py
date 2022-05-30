# -*- coding: utf-8 -*-
"""
Created on Mon May 30 19:01:52 2022

@author: HENRY
"""

from Lecturer import Lecturer

L = Lecturer("Prof. ", 'William',' Kariuki',3463,"APP 4010")

L.get_course() 

L.set_course("APT3030")

L.get_name()

print(L)

L2 = Lecturer("Dr. ", "Sharon ","Wanyama", 475373,"IST3050")

L2.get_course()

L2.set_course("GRM2000")

L2.get_name()

print(L2)
