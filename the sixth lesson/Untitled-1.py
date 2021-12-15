# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Окно")
window.geometry('1200x300')

tab_control = ttk.Notebook(window)
z1 = ttk.Frame(tab_control)
z2 = ttk.Frame(tab_control)
z3 = ttk.Frame(tab_control)
z4 = ttk.Frame(tab_control)
z5 = ttk.Frame(tab_control)
z6 = ttk.Frame(tab_control)
z7 = ttk.Frame(tab_control)
z8 = ttk.Frame(tab_control)

def prgr1():
    a = t1.get()
    i = 1
    N = int(a)
    result = ""
    while i ** 2 < N:
        result += str(i**2)
        i+=1
        result = result + " "
    o1.configure(text = result)
tab_control.add(z1, text='Задание 1')
l1 = Label(z1, text='По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.')
l1.grid(column=0, row=0)
lz1 = Label(z1, text='Введите N :')
lz1.grid(column=0, row=1, sticky=W)
t1 = Entry(z1, width=20)
t1.grid(column=0, row=1, sticky=W)
t1.place(x=70, y=20)
b1 = Button(z1, text="Ответ", command=prgr1)
b1.grid(column=0, row=2, sticky=W)
v1 = Label(z1, text = 'Результат :')
v1.grid(column=0, row=3, sticky=W)
o1 = Label(z1, text="")
o1.grid(column=0, row=4, sticky=W)
    
def prgr2():
    a = t2.get()
    n = int(a)
    i = 2 
    while n % i !=0:
        i += 1
    o2.configure(text = i)
tab_control.add(z2, text='Задание 2')
l2 = Label(z2, text='Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.')
l2.grid(column=0, row=0)
lz2 = Label(z2, text='Введите целое число, не меньшее 2 :')
lz2.grid(column=0, row=1, sticky=W)
t2 = Entry(z2, width=20)
t2.grid(column=0, row=1, sticky=W)
t2.place(x=210, y=20)
b2 = Button(z2, text="Ответ", command=prgr2)
b2.grid(column=0, row=2, sticky=W)
v2 = Label(z2, text = 'Результат :')
v2.grid(column=0, row=3, sticky=W)
o2 = Label(z2, text="")
o2.grid(column=0, row=4, sticky=W)
def prgr3():
    a = t3.get()
    n = int(a)
    i = 2
    e = 1
    while i <= n:
        i*=2
        e+=1
    result="Степень :" +str(e-1) +" "+"Число :" +str(i//2)
    o3.configure(text=result)
tab_control.add(z3, text='Задание 3')
l3 = Label(z3, text='По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N. \nВыведите показатель степени и саму степень. Операцией возведения в степень пользоваться нельзя!')
l3.grid(column=0, row=0)
lz3 = Label(z3, text='Введите N :')
lz3.grid(column=0, row=1, sticky=W)
t3 = Entry(z3, width=20)
t3.grid(column=0, row=1, sticky=W)
t3.place(x=70, y=40)
b3 = Button(z3, text="Ответ", command=prgr3)
b3.grid(column=0, row=2, sticky=W)
v3 = Label(z3, text = 'Результат :')
v3.grid(column=0, row=3, sticky=W)
o3 = Label(z3, text="")
o3.grid(column=0, row=4, sticky=W)
def prgr4():
    x = int(tx4.get())
    y = int(ty4.get())
    n=1
    while x<y:
        x*=1.1
        n+=1
    n = str(n) + "дней"
    o4.configure(text=n)
tab_control.add(z4, text='Задание 4')
l4 = Label(z4, text="ППрограмма получает на вход действительные числа x и y и должна вывести одно натуральное число")
l4.grid(column=0, row=0, sticky=W)
lz4 = Label(z4, text='Введите x и y :')
lz4.grid(column=0, row=1, sticky=W)
tx4 = Entry(z4, width=20)
tx4.grid(column=0, row=1, sticky=W)
tx4.place(x=90, y=50)
ty4 = Entry(z4, width=10)
ty4.grid(column=0, row=1, sticky=W)
ty4.place(x=140, y=50)
b4 = Button(z4, text="Ответ", command=prgr4)
b4.grid(column=0, row=2, sticky=W)
v4 = Label(z4, text = 'Результат :')
v4.grid(column=0, row=3, sticky=W)
o4 = Label(z4, text="")
o4.grid(column=0, row=4, sticky=W)
k=0
def prgr5():
    global k
    a = t5.get()
    print(a)
    if (a!="0"):
        k += 1
    else: 
        o5.configure(text=k)
    t5.delete(0, END)
tab_control.add(z5, text='Задание 5')
l5 = Label(z5, text="Пос-ть завершается числом 0, при считывании которого программа должна закончить свою работу и вывести количество членов последовательности")
l5.grid(column=0, row=0)
lz5 = Label(z5, text='Введите число :')
lz5.grid(column=0, row=1, sticky=W)
t5 = Entry(z5, width=20)
t5.grid(column=0, row=1, sticky=W)
t5.place(x=90, y=50)
b5 = Button(z5, text="Ответ", command=prgr5)
b5.grid(column=0, row=2, sticky=W)
v5 = Label(z5, text = 'Результат :')
v5.grid(column=0, row=3, sticky=W)
o5 = Label(z5, text="")
o5.grid(column=0, row=4, sticky=W)
x=0
y=0
def prgr6():
    global y 
    a = t6.get()
    print(a)
    global x
    if a !="0":
        y += 1
        x +=int(a)
    else:
        o6.configure(text=x/y)
    t6.delete(0,END)
tab_control.add(z6, text='Задание 6')
l6 = Label(z6, text="Cреднее значение всех элементов последовательности, завершающейся числом 0")
l6.grid(column=0, row=0)
lz6 = Label(z6, text='Введите число :')
lz6.grid(column=0, row=1, sticky=W)
t6 = Entry(z6, width=20)
t6.grid(column=0, row=1, sticky=W)
t6.place(x=90, y=20)
b6 = Button(z6, text="Ответ", command=prgr6)
b6.grid(column=0, row=2, sticky=W)
v6 = Label(z6, text = 'Результат :')
v6.grid(column=0, row=3, sticky=W)
o6 = Label(z6, text="")
o6.grid(column=0, row=4, sticky=W)
b=0
a=10000000
def prgr7():
    n=t7.get()
    print(n)
    global b
    global a
    if(int(n) > a):
        b+=1
    a = int(n)
    if(n=="0"):
        o7.configure(text=b)
    t7.delete(0, END)
tab_control.add(z7, text='Задание 7')
l7 = Label(z7, text="Сколько элементов этой последовательности больше предыдущего элемента:")
l7.grid(column=0, row=0)
lz7 = Label(z7, text='Введите N :')
lz7.grid(column=0, row=1, sticky=W)
t7 = Entry(z7, width=20)
t7.grid(column=0, row=1, sticky=W)
t7.place(x=70, y=20)
b7 = Button(z7, text="Ответ", command=prgr7)
b7.grid(column=0, row=2, sticky=W)
v7 = Label(z7, text = 'Результат :')
v7.grid(column=0, row=3, sticky=W)
o7 = Label(z7, text="")
o7.grid(column=0, row=4, sticky=W)
def prgr8():
    c = 1
    m = 0
    l = 0
    while True:
        x=l.get()
        if x == 0:
            break
        if(l != 0):
    
            if(x == p):
                c += 1
            else:
                if(m < c):
                    m = c
                c = 1
        p = x
        l+=1
    o8.configure(text=max(m, c))
    t8.delete(0, END)
tab_control.add(z8, text='Задание 8')
l8 = Label(z8, text="Сколько элементов этой последовательности больше предыдущего элемент:")
l8.grid(column=0, row=0)
lz8 = Label(z8, text="Введите N:")
lz8.grid(column=0, row=1, sticky=W)
t8 = Entry(z8, width=20)
t8.grid(column=0, row=1, sticky=W)
t8.place(x=70, y=20)
b8 = Button(z8, text="Ответ:", command=prgr8)
b8.grid(column=0, row=2, sticky=W)
v8 = Label(z8, text = "Ответ:")
v8.grid(column=0, row=3, sticky=W)
o8 = Label(z8, text="")
o8.grid(column=0, row=4, sticky=W)

tab_control.pack(expand=1, fill='both')
window.mainloop()