# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 20:19:54 2019

@author: aleci
"""
n=50
#First terms of the sequence 
first = 0
second = 1
mylist = []
#print('The Fibonnacci series is:')
print(first,' ,', second, end=",")
print('These are the last 15 terms of the squence:',mylist[-15:])
for ii in range (0,n):
    next = first + second
    print(next)
   

    first = second
    second = next




