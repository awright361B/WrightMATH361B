# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:39:19 2019

@author: aleci
"""

N=50
terms = [0,1]
multi = 30
my_list=[]
m=[]

for ii in range(2,N):
    f = terms [ii-1] + terms [ii-2]
    terms.append(f)
    

if(f % 30==0):
    my_list.append(ii)

length = (30)
percentage=(length/50)

print(percentage,m)

