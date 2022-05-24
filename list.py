# -*- coding: utf-8 -*-
"""
Created on Tue May 24 16:08:56 2022

@author: boloka
"""
n=5
scores = []
for i in range(n):
    score = float(input("Enter a score:  "))
    scores.append(score)
    
 
    print(scores)

total = 0
for item in scores:
    total = total + item
print("The average for the class is",total/n)