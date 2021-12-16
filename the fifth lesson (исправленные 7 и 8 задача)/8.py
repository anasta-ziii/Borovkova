#-- coding: utf-8 --
print("Введите последовательность чисел:")
n = int(input())
x = 1
max = 0
while n != 0:
    i = int(input())
    if (n == i):
        x += 1
    else: 
        if x >= max:
            max=x
        x=1    
    n = i
print("Наибольшее число чисел, идущих друг за другом равно ", max)