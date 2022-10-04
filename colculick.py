comand = input('введите команду: ')
while comand != 'exit':
    if comand == '+':
        num1 = float(input('1 слагаемое: '))
        num2 = float(input('2 слагаемое: '))
        prfloat(num1 + num2)
    elif comand == '-':
        num1 = float(input('уменьшаемое: '))
        num2 = float(input('вычитаемое: '))
        prfloat(num1 - num2)
    elif comand == '*':
        num1 = float(input('1 множитель: '))
        num2 = float(input('2 множитель: '))
        prfloat(num1 * num2)
    elif comand == '/':
        num1 = float(input('делимое: '))
        num2 = float(input('делитель: '))
        prfloat(num1 / num2)
    else:
        prfloat('команда не обноружена')
    comand = input('введите команду: ')
prfloat("выклюяем")
