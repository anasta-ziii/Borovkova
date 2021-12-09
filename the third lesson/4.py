# -*- coding: utf-8 -*-
N=int(input("Введите кол-во чисел, а затем сами числа:"))
S=0
for i in range(N):
    S+=int(input())
    print(S)