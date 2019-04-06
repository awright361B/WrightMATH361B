# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:38:03 2019

@author: aleci
"""

import numpy as np
P = 5

def prime_check(x):
    prime = True 
    for ii in range (2,x): 
        mod = x%ii
        if (mod !=0): 
            prime = True
        elif (mod ==0): 
            prime = False
            break
        return prime
print(prime_check)
    
np.array([0,2])
count = 1
for i in range (2,P): 
    for n in range(0,P-1,P):
        for k in range (0,P-1, P):
             n = k**2 
             
I am not sure where to go from here!!! I was to stressed and gave up.
I did not want to use Ben's code from class since I did not understand it.        