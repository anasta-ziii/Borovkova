age=18
name='Иван'
if age>0 and age<75:
    if age>=16:
        if name is 'Иван':
            print('Смените имя')
        else:
            print('Поздрвляем вы поступили в ВГУИТ!')
    else: 
        print('Сначала нужно окончть школу!')
        print(18-age,'лет осталось учиться в школе')
else: 
    print('Ошибка в age')