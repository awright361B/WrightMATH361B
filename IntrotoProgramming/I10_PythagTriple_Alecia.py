# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:09:26 2019

@author: aleci
"""


import numpy as np 
#define pythagorean triple
def pythagorean_triple(n):
#create forloop here for b
    for b in range(1,n):
# inner loop for a
        for a in range(1,n):
#import np.sqrt to find 1026
            c = np.sqrt ( a**2 + b**2)
            if c % 1 == 0: 
# c is an integer int(c)
                print (a, b, int(c))
                break

pythagorean_triple(500)
print ("The pythagorean triple is 297, 304, 425")

x= np.array( [[297, 304, 425], [405, 216, 495], [175,420,455] ])
my_array = np.zeros([3,4])
x = np.vstack( [x, np.array( [ 1026, 1116, 1050] ) ] )
print(x)


