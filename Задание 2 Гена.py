import math

print('''Список функций:
Сложение(+), вычитание(-), умножение(*), деление(/), возведение в степень(**), логарифм(log), 
округление в большую сторону до N знака после запятой(ceil), округление в меньшую сторону 
до N знака после запятой(floor), конец(end)''')
function = input('Введите функцию:')

while function != 'end':
    if function == '+':
        x = float(input('Введите первое число:'))
        y = float(input('Введите второе число:'))
        print(x + y)
    elif function == '-':
        x = float(input('Введите первое число:'))
        y = float(input('Введите второе число:'))
        print(x - y)
    elif function == '*':
        x = float(input('Введите первое число:'))
        y = float(input('Введите второе число:'))
        print(x * y)
    elif function == '/':
        x = float(input('Введите первое число:'))
        y = float(input('Введите второе число:'))
        print(x / y)
    elif function == '**':
        x = float(input('Введите первое число:'))
        y = float(input('Введите второе число:'))
        print(x ** y)
    elif function == 'log':
        x = float(input('Введите аргумент:'))
        y = float(input('Введите основание:'))
        print(math.log(x, y))
    elif function == 'ceil':
        x = float(input('Введите число:'))
        print(math.ceil(x))

    elif function == 'floor':
        x = float(input('Введите число:'))
        print(math.floor(x))
    elif function == 'end':
        print('Конец программы')
    else:
        print('Неизвестная функция, попробуйте еще раз')
