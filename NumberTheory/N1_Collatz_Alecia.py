# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 13:53:11 2019

@author: aleci
"""



def printcollatz(a): 
      #create a while loop
    while a != 1: 
        print(a, end = ' ') 
   # n is odd  
        if a & 1: 
            a = 3 * a + 1
  # n is even 
        else: 
            a = a // 2
   
    print(a) 

print("The terms of the sequence are")
printcollatz(600)

  
        




        
    