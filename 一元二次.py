#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 22:15:28 2024

@author: chenbailun
"""

def equation(a,b,c):
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + D ** 0.5) / (2*a)
        x2 = (-b - D ** 0.5) / (2*a)
        return [x1,x2]
    elif D == 0:
        x = -b / (2 * a)
        return [x]
    else:
        return ["無解"]
a = float(input("enter a:"))
b = float(input("enter b:"))
c = float(input("enter c:"))
sol = equation(a,b,c)
print("解:",sol)