# -*- coding: utf-8 -*-
from  tkinterimport *
from tkintertkinter import ttk

def d1():
    arg = txt.get()
    i = 1
    N = int(arg)
    R = ""
    while i * i <= N:
        i+=1
        R += str(i)
    messagebox.showinfo("Ответ:", R)

def d2():
    arg = txt1.get()
    i = 2
    N = int(arg)
    while N % i != 0:
        i += 1
    messagebox.showinfo("Ответ:", i)

def d3():
    arg = txt2.get()
    N = int(arg)
    alll = 2
    step = 1
    while alll <= N:
        alll *= 2
        step += 1
    messagebox.showinfo("Ответ:", "Степень:" + str(step - 1) + " " + "Пок-ль степени:" + str(alll // 2))

def d4():
    x = int(txt3_1.get())
    y = int(txt3_2.get())
    N = 1
    while x < y:
        x *= 1.1
        N+= 1
    messagebox.showinfo("Ответ:", N)
u0c1 = 0

def d5():
    global u0c1
    arg = txt4.get()
    if(arg != "0"):
        u0c1 += 1
    else:
        messagebox.showinfo("Ответ:", u0c1)
        u0c1 = 0
    txt4.delete(0, END)

u0c2 = 0
summ = 0

def d6():
    global u0c2
    global summ
    arg = txt5.get()
    if arg != "0":
        u0c2+=1
        summ += int(arg)
    else:
        messagebox.showinfo("Ответ:"'Ответ: ', summ/u0c2)
        u0c2 = 0
        summ = 0
    txt5.delete(0, END)

u0c3 = 0
cn = 999999999


def d7():
l7 = Label(z7, text='Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности больше предыдущего элемента.')
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

def d8():
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

l8 = Label(z8, text='Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности больше предыдущего элемента.')
l8.grid(column=0, row=0)
lz8 = Label(z8, text='Введите N :')
lz8.grid(column=0, row=1, sticky=W)
t8 = Entry(z8, width=20)
t8.grid(column=0, row=1, sticky=W)
t8.place(x=70, y=20)
b8 = Button(z8, text="Ответ", command=prgr8)
b8.grid(column=0, row=2, sticky=W)
v8 = Label(z8, text = 'Результат :')
v8.grid(column=0, row=3, sticky=W)
o8 = Label(z8, text="")
o8.grid(column=0, row=4, sticky=W)

tab_control.pack(expand=1, fill='both')
window.mainloop()