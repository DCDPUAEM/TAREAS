#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 21:29:36 2022

@author: Alec.B.N
"""


#Ejercicio Fizz Buzz

n = int(input("Hasta que numero deseas jugar: "))
i = 1
while i <= n:
    if i%3 == 0 and i%5 == 0:
        print("FizzBuz", end = ' ')
        i = i + 1 
    elif i%3 == 0:
        print("Fizz", end = ' ')
        i = i + 1 
    elif i%5 == 0:
        print("Buzz", end = ' ')
        i = i + 1 
    else:
        print(i, end = ' ')
        i = i + 1
        
print("Juego terminado :)")