" Eladio"
valorInicial=1
valorFinal=30

for i in range(valorInicial,valorFinal+1):
    
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
        " multiplo de 3 y de 5"
    elif (i % 3 == 0):
        print("Fizz")
        " multiplode 3 "

    elif (i % 5 == 0):
        print("Buzz")
        " multiplo de 5"
        
    else:
        print(i)
        " cualquier otro número"


