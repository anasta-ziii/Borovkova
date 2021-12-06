# -*- coding: utf-8 -*-
print('Задание #6')
print()
n=int(input("Введите число:"))
l=0
k=0
while n!= 0:
    k+=n
    n=int(input("Введите число:"))
    l+=1
print("Среднее значение =:",k/l)