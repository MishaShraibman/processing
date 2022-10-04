comand = input('введите команду: ')
while comand != 'exit':
    if comand == '+':
        num1 = int(input('1 слагаемое: '))
        num2 = int(input('2 слагаемое: '))
        print(num1 + num2)
    elif comand == '-':
        num1 = int(input('уменьшаемое: '))
        num2 = int(input('вычитаемое: '))
        print(num1 - num2)
    elif comand == '*':
        num1 = int(input('1 множитель: '))
        num2 = int(input('2 множитель: '))
        print(num1 * num2)
    elif comand == '/':
        num1 = int(input('делимое: '))
        num2 = int(input('делитель: '))
        print(num1 / num2)
    else:
        comand = input('введите команду: ')