# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 12:01:05 2019

@author: aleci
"""
N = 12

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
    

prime_list =[2]
for kk in range(3, 1000): 
    primality = prime_check(kk)
    if(primality == True):
        prime_list.append(kk)
        if (len(prime_list) == N):
            break
    
print("The", N, "th prime number is", prime_list[-1])
