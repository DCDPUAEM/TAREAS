# -*- coding: utf-8 -*-
"""
Spyder Editor

Ejercicio FizzBuzz Eduardo Rodríguez de San Miguel Guerrero
"""

inicio = input("Ingrese el número entero inicial de la secuencia: ")
fin = input("Ingrese el número entero final de la secuencia: ")

inicio = int(inicio)
fin = int(fin)

for fizzbuzz in range(inicio, fin + 1):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("FizzBuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("Fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("Buzz")
        continue
    print(fizzbuzz)