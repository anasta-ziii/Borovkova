a = int(input("Расстояние между рядами: "))
b = int(input("Расстояние между дырочками в ряду: "))
L = int(input("Длина свободного конца шнурка: "))
N = int(input("Количество дырочек в каждом ряду: "))
 защита (a, b, L, N):
    возврат (2 * L + (2 * N - 1) * a + 2 * (N - 1) * b)
print ("Ответ: ", dlina (a, b, L, N)) 

печать("\n") 