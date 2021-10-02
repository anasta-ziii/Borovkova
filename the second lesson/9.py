# -- coding: utf-8 --
def chocolad():
    print("Введите размер шоколадки - длину и ширину:")
    n = int(input())
    m = int(input())
    print("Введите из скольки долек должна состоять отломленная часть шоколадки:")
    k = int(input())
    if k % n == 0:
        return "Да"
    else:
        return "Нет"
print(chocolad())