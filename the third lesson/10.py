
# -- coding: utf-8 --
def sum_fib():
    N = int(input("Введите кол-во чисел из ряда Фибоначчи:"))
    K = int(input("Введите порядковый номер в ряду, с которого нужно начать:"))
    first = 0
    second = 1
    sum = 0
    if K < 3:
        sum += 1
    for i in range(2, N):
        num = first + second
        first, second = second, num
        if i >= (K-1):
            sum += num
    print(sum)
sum_fib()