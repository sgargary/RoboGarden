# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:51:40 2019

@author: Sahar

"""
sum = 0
for x in range (5):
       
        sum = sum + int(input ("Enter a number in the range from 0 to 20: "))
#scores = int(input("5"))
if sum < 50:
        grade = "F"
elif sum < 65:
        grade = "D"
elif sum < 75:
        grade = "C"
elif sum < 85:
        grade = "B"
elif sum > 85:
        grade = "A"
        
    

            