# -*- coding: utf-8 -*-
"""
Created on Tue May 17 16:23:10 2022

@author: boloka
"""

receipt= float(input("Enter the receipt amount: "))
total = 0
while receipt != -1:
    total = total + receipt
    receipt= float(input("Enter the receipt amount or -1 to quit"))
    
print("The total is", total)