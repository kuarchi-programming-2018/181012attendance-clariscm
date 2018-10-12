# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 17:12:34 2018

@author: daiyuhua
"""

def fib(n):
    return n

    FP=[0,1]
    if n>=2:
        for i in range(2,n+1):
            FP.append(FP[i-2]+FP[i-1])
    print(FP[n])
    
fib(5)
