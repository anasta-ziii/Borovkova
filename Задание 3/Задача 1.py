A = int(input("Введите первое число:"))
B = int(input("Введите второе число:"))
if A>B:
 for i in range(A - (A + 1) % 2, B - B % 2, -2):
    print(i, end=' ')
else:
  print("ошибка!")