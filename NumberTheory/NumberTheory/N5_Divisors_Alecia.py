# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:07:28 2019

@author: aleci
"""

def d (x):
    l = []
    for i in range (1,x-1): 
        if x/i == int(x/i): 
            l.append(i)
    print(l)
d(10)
d(30)