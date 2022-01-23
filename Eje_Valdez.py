# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 17:36:43 2022

@author: jsvaldezmtz
"""

# EJERCICIO FIZZ BUZZ

print('Dame el primer numero: ')
n=int(input())

print('Dame el segundo numero: ')
m=int(input())

print('La numeracion sera desde',n,'hasta',m)
otra_n = n

while otra_n<=m:
    if otra_n%3 == 0:
        print('Fizz',end=' ')
    if otra_n%5 == 0:
        print('Buzz',end=' ')
    else:
        print(otra_n, end= ' ')    
    otra_n += 1

print('\n')
secuencia = range(n,m+1)
for i in secuencia:
    if i%3 == 0:
        print('Fizz',end=' ')
    if i%5 == 0:
        print('Buzz',end=' ')
    else:
        print(i, end= ' ')
