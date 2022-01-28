# -*- coding: utf-8 -*-
"""Ejercicio_FizzBuzz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S1Slr2LGLGW7qhLijOMBawevsDVOuQQw

Ejercicio 1:  Alumno Carlos Pineda-Antunez

Ejercicio Fizz Buzz

Fizz buzz es un juego de palabras grupal para enseñar a los niños la división [1]. Los jugadores se turnan para contar de forma incremental, reemplazando cualquier número divisible por tres con la palabra "Fizz" y cualquier número divisible por cinco con la palabra "Buzz".

================================================================================
"""

#Ejercicio FizzBuzz
#Elaboró: Carlos Pineda-Antunez
#Datos de entrada
numeros=input("Ingresa el numero minimo y el numero maximo")
numeros=numeros.split()
num_min= int(numeros[0])
num_max= int(numeros[1])
word_tres="Fizz" 
word_cinco="Buzz"

# Ciclo para la colocación de "FIzz Buzz"
for i in range(num_min,num_max):
  if i%3 == 0 and i%5 == 0 : 
    print(word_tres+" "+word_cinco)
  elif  i%3 == 0:
        print(word_tres)
  elif  i%5 == 0:
        print(word_cinco)
  else :
    print(i)