# -*- coding: utf-8 -*-
"""
Created on Tue May 24 16:34:42 2022

@author: boloka
"""

x = [1,2,3,4]
y = [3,5,2,7]
p = [1,3,5,6]

z = []

for item1 in x:
    for item2 in y:
        z.append([item1, item2])
        
print(z)

print ()

#Using a list comprehension

a = [[b,c, d] for b in x for c in y for d in p if b!= c if c!=d]

print (a)