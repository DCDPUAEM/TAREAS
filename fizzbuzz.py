# -*- coding: utf-8 -*-
"""FizzBuzz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17RvkiG8CBTzHA1tJx-dLdJZIYa3OZG7u

## Ejercicio Fizz Buzz
"""

#Intrucciones
print('Vamos a jugar Fizz Buzz')
print('''Escribiré Fizz cuando encuentre un numero divisible entre tres y 
Buzz cuando el número sea divisible entre 5''')
print('Vamos a jugar...Crearemos la lista de números con la que vamos a jugar')


#Obtenemos los números
print('Dame el primer número de la lista: ')
x=int(input())
print('Dame el último número de la lista: ')
y=int(input())

#Verificamos la longitud de la lista
dif = y - x
if dif == 0:
    print('No puedo jugar...Dame una lista más grande')
    while dif < 3:
       print('El primer número de la lista es: ', x)
       m = x + 3
       print(f'Dame un nuevo último número para la lista mayor a {m} : ')
       y=int(input())
       dif = y - x
elif dif <= 2:
    print('Son muy pocos numeros, intenta una secuencia más larga...')
    while dif < 3:
       print('El primer número de la lista es: ', x)
       m= x + 3
       print(f'Dame un nuevo último número para la lista mayor a {m} : ')
       y=int(input())
       dif= y - x
print(f'La secuencia es de {x} a {y}.')

#Iniciamos la sustitucion de valores
for i in range(x,y):
   if i%3 == 0 and i%5 == 0:
      nueva.append('Fizz Buzz')
   elif i%3 == 0:
      nueva.append('Fizz')
   elif i%5 == 0:
      nueva.append('Buzz')
   else:
        nueva.append(str(i))
print('La nueva lista es: ', nueva)