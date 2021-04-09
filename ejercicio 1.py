# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 20:26:21 2021

@author: 200027302
"""
lista1 = [0,1,2,"I",3,4,5]
print(lista1)
print(lista1[0:4])
print(lista1[-3:-1])
print(len(lista1))
lista1.append("UMAYOR")
lista1.insert(1,"Python")
lista1.remove(0)
lista1.pop(3) 
lista1.clear()


print(lista1)
nuevalista1= lista1.copy()
print(nuevalista1)