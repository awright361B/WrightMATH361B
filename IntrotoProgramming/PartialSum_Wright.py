# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 17:34:36 2019

@author: aleci
"""

import numpy as np 

n= 100 
s= 0
sa=[]
t= 0
tb=[]
p = 0
pc=[]

for ii in range (1,n):
    s+= (np.log(ii**4+ii+3)/(np.sqrt(ii)+3))
    sa.append(s)
#print(sa)
#print(s)
print('This is the first fifteen',sa[:15])
print('This is the last fifteen', sa[-15:])

for ii in range (1,n):
    t+= (np.exp(ii/100)/(ii**10))
    tb.append(t)
print(tb)
print(t)
print ('This is the first fifteen', sa[:15])
print('This is the last fifteen', sa[-15:])

for ii in range (1,n):
    p+= (np.exp(ii/ii**2)+ii**5)
    pc.append(p)
print(pc)
print(p)
print('This is the first fifteen', sa[:15])
print('This is the last fifteen', sa[-15:])
