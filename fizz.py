#programa fizz buzz fizzbuzz

contar = int(input("hasta que numero quieres contar"))

for contar in range(1,contar+1):
    if contar % 3 ==0 and contar % 5 ==0:
        print(f"{contar} fizzbuzz")
    elif contar % 5 ==0:
        print(f"{contar} buzz")
    elif contar % 3 ==0:
        print(f"{contar} fizz")
    else:
        print(f"{contar}")
