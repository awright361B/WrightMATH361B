# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:04:29 2019

@author: aleci
"""


def prime_check(x): 
    l = []
    v = []
    for i in range(2,N): 
        if N/i == int(x/i): 
            l.append(x)
            break
    if len (l) == len(v): 
        return(True)
    else: 
        return(False)
        

N= 60


for nn in range(4,N,2): 
    GB_check = False
    
    #Need to find p_1 and p_2 primes so that n = p_1 + p_2
    for p1 in range(1,nn):
        if (prime_check (p1) == False):
            continue
        if (prime_check (nn-p1) == True): 
            GB_check = True
    if (GB_check == True):
        print(nn)


            
        
        



