# -*- coding: utf-8 -*-
"""
Created on Tue May 17 16:03:25 2022

@author: boloka
"""

mark = int(input("Enter a numeric mark: "))
if mark >= 90 :
    grade = "A"
elif mark >= 80:
    grade = "B"
elif mark >=70:
    grade = 'C'
elif mark >=60:
    grade = 'D'
else:
    grade = 'F'

print("The grade is", grade)    
