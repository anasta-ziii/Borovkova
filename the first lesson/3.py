# -- coding: utf-8 --
name = input ('Ваше имя: ')
age = int (input ('Ваш возраст = '))
if 0<age<75 and name != 'Иван' and name != 'иван':
    if age > 16:
        print ('Поздравляем вы поступили в ВГУИТ!')
    elif age < 16:

        ost = 16 - age
        print ("Вам нужно окончить школу, тебе осталось учиться:",ost)
else:
    print('не подходите')