# -- coding: utf-8 --
a = int(input("Ведите А:"))
b = int(input("Ведите B:"))
if a<b:
    for i in range (a, b+1):
        print(i)
else:
    for i in range (a, b-1, -1):
        print(i)