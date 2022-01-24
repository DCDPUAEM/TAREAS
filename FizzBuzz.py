#Luis David Rodríguez Padilla

a = int(input())
b = int(input())

lista = [x if x%3!=0 and x%5!=0 else "FIZZ BUZZ" if x%5==0 and x%3==0 else "FIZZ" if x%3==0 else "BUZZ" for x in range(a,b)]

print(lista)

