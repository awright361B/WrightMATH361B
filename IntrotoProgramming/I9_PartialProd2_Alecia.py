# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:25:08 2019

@author: aleci
"""

import numpy as np

N = 20
a_n = lambda n:  1+ (f_n(n)/g_n(n))
f_n = lambda n: 1/(n**2 + 5)
g_n = lambda n: n**5 + 12
seq = np.array([a_n(1)]) 

for ii in range(2,N):
    term = ([seq[-1]*a_n(ii)])
    seq = np.append(seq, term)

print('These are the first fifteen terms', seq[:15])
print('These are the last fifteen terms', seq[-15:])

b = 20
a_n = lambda n: 1 + b**n
seq = np.array([a_n(1)])

for jj in range (2,N):
    term = ([seq[-1]*a_n(jj)])
    seq = np.append(seq,term)
    
print("These are the first fifteen terms", seq[:15])
print("These are the last fifteen terms",seq[-15:])



