A = int(input("Введите первое число A:"))
B = int(input("Введите второе число B, которое меньше А:"))
if A>B:
 for i in range(A - (A + 1) % 2, B - B % 2, -2):
    print(i)
else:
  print("ошибка!")