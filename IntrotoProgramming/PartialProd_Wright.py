# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 19:34:03 2019

@author: aleci
"""

import numpy as np

n=100
p= 0
pa=[]
q= 0
qb=[]
r = 0
rc=[]

for ii in range (1,n):
    p+= ((np.array(ii**3-1))/(np.array(ii**3+1)))
    pa.append(p)
#print(pa)
#print(p)
print('This is the first fifteen terms', pa[:15])
print('This is the last fifteen terms', pa[-15:])

for ii in range(1,n): 
    q+= ((np.exp(ii/100))/(ii**10))
    qb.append(q)
#print(qb)
#print(q)
print('This is the first fifteen terms', qb[:15])
print('This is the last fifteen terms', qb[-15:])

for ii in range (1,n):
    r+=((np.array(ii**5)/np.array(ii**10+3)))
    rc.append(r)
#print(rc)
#print(r)
print('This is the first fifteen terms', rc[:15])
print('This is the last fifteen terms', rc[-15:])
