# -*- coding: utf-8 -*-
print('Задание #8')
def n():
    counter=1
    maxS=0
    lc=0
    while True:
        x=int(input("Введите число:"))
        if x==0:
            break
        if(lc!=0):
            if(x == container):
                counter += 1
            else:
                if(maxS<counter):
                    maxS=counter
                counter=1
        container=x
        lc+=1
    print(max(maxS, counter))

n()