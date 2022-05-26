# -*- coding: utf-8 -*-
"""
Created on Thu May 26 16:05:10 2022

@author: boloka
"""

from person import Person 
from student import Student

p1 = Person('Ben','Afleck',374037)

print(p1.get_first(),p1.get_last(),p1.get_ID())

p2 = Person('Ryan', 'Renolds', 203940)
print(p2.get_first(),p2.get_last(),p2.get_ID())

p3 = Person('Dr','Strange',836492)

print(p3.get_first(),p3.get_last(),p3.get_ID())
p4 = Person('Mr','Odhiambo',283949)
print(p4.get_first(),p4.get_last(),p4.get_ID())
print("We have",p2.get_count(),"people. ")

s = Student('Oerant ','Gaddhafi',384940,"jkuat","International relations")

print(s.get_name(), s.get_ID(), s.get_school(),s.get_major())
print(s)
