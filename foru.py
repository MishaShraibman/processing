import time

#начало и помощь
print('привет я помошник')
time.sleep(1)
print('для начала команды для меня')
time.sleep(1)
pomosh = ['удалить по названию "удалть1"','удалить по индексу "удалить2"','добавить команду "добавить"','показать таблицу "view"']
for elem in pomosh:
    print(elem)

#сам список
mylist = ['апельсин', "помидор", "твой друг"]
print('так же всё в списке по умолчанию')
for elem in mylist:
    print(elem)

#выбор пользователя
a = (input('что хочешь сделать?: '))
while a != 'stop':
    if a == 'удалить1':
        mylist.remove(input('какой элемент нужно удалить?: '))
        a = input("что дальше?: ")
        
    elif a == 'удалить2':
        mylist.pop(int(input('какой элемент нужно удалить?: ')))
        a = input("что дальше?: ")
        
    elif a == 'добавить':
        mylist.append(input('добавьте элемент: '))
        a = input('что дальше?: ')
        
    elif a == 'view':
        for elem in mylist:
            print(elem)
        a = input('что дальше?: ')
            
    else:
        print("братан ты на приколе? ну рил давай нормально")
print('s[hoeirtg')