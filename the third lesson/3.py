# -- coding: utf-8 --
a = int(input("Введите А:"))
b = int(input("Введите B, которое < А:"))
for i in range (a, b-1, -1):
    if i % 2 !=0:
        print (i)