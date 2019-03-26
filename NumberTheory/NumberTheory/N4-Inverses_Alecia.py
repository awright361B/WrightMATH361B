# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 12:26:45 2019

@author: aleci
"""


def modulo_multiplicative_inverse(A,M): 
    for ii in range(0,M):
        if (A*ii) % M == 1:
            return ii 
        

print(modulo_multiplicative_inverse(5,11))
print(modulo_multiplicative_inverse(3, 20))

    