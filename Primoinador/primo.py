num1 = int(input())
num2 = int(input())
def nprimos():
    cont = 0
    for i in range(num1, num2 + 1):
        primos = True
        for j in range(2, 10):
            if i == j:
                break
            elif i % j == 0:
                primos = False
            else:
                continue
        if primos == True:
            resultado = print(' ', i, end='')
            cont += 1

    if num1 >= num2:
        while num1 != 33 and num2 != 12:
            print("El primer número indicado debe ser mayor")
            break
        if num1 == 33 and num2 == 12:
            print("Iniciando Autodestrucción...")