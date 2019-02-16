# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:00:38 2019

@author: aleci
"""
import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    if x < -2:        
        f = -3*(x+2)**2 +1 
    elif -2 <= x and x < -1:
        f = 1
    elif -2 <= x and x < -1:
        f = (x-1)**3 + 3
    elif -1 <= x and x < 1:
       f = (np.sin(np.pi)*x +3)
    elif 1 <= x and x <2 :
        f = 3 * math.sqrt(x-2) +4
    elif x >= 2:

        x = np.linespace( -3, 3) 
        y = f(x)
        
for ii in (N):
            y = np.append(f(x)

plt.plot(x,y)
plt.show()

#I am not to sure what is wrong with the code at the end. I thought everything was right but apprarently not. 


