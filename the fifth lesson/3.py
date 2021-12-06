# -- coding: utf-8 --
print('Задание 3')
print()
n=int(input('Введите любое число: '))
m=1
i=0
while m<n:
    if m*2>n:
     break
    m*=2
    i+=1
print(m)