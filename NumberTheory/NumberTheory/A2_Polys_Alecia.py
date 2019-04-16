# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 22:32:26 2019

@author: aleci
"""
#poly1d= polynomial respresentation
#polyder= derivative
#polyint - integral
import numpy as np

def p(x): 
    4*x**3+3*x**2 -2*x +1

#evaluate a polynomial at a given point
def p(x):
     4*x**3+3*x**2 -2*x +1
p = np.poly1d([4, 3, -2, 1])
print("The polynomial evaluated at 3 is", p(3))

#derivative of a polynomial 
p = np.poly1d([4, 3, -2, 1])
p1 = np.polyder(p)
print("The derivative of the polynomial is", (p1))

#Integral of a polynomial 
p = np.poly1d([4,3,-2,1])
p1 = np.polyint(p)
print ("The integral of the polynomial with an upper bound of 3 and lower bound of 2 is", p1(3) - p1(2))


