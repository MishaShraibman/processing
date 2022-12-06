import time
import random
import pyautogui

note1 = ''
note2 = ''
note3 = ''

print('здравствуйте, я бот-помощник. советую сначала обратиться к команде "помощь"')
time.sleep(1)
comand = input("введите команду: ")

#для рандома
anekdot = ["колобок повесился","ты алмаз в моей жизни... такой же глупый непробиваемый","ты мой ангел. типа с небес спустился? типа парашют не раскрылся"]
skazka = ["неа, мне лень","жили как то рак щука и осёл. рак был синий, щука зелёный а олень бесцветным..."]

#действия
while comand != 'выход':
    if comand == 'помощь':
        print('"анекдот" - рассказывает анекдот')
        print('"сказка на ночь" - я думаю понятно')
        print('"важная новость" - рассказывает важные и свежие новости')
        print('"записки" - показывает написанные заметки')
        print('"создание заметки" - пиши чё хош')
        print('"запомнить контакт" - ФИО + номер телефона (без плюса)')
        print('"выход" - закрывает меня')
        print('"prize" - kaboom (ломает всё, не советую)')
        comand = input("введите команду: ")
    elif comand == 'анекдот':
        print(random.choice(anekdot))
        comand = input('введите следующую команду: ')
    elif comand == 'сказка на ночь':
        print(random.choice(skazka))
        comand = input('введите следующую команду: ')
    elif comand == 'важная новость':
        print('гена решил что пора наконец двигаться дальше и прошёл ещё 2 метра вперёд и устал... АКЦИЯ, ТОЛЬКО СЕГОДНЯ, В ПЯТЁРОЧКЕ!')
        comand = input('введите следующую команду: ')
    elif comand == 'записки':
        hmm = int(input('какую заметку хотите прочитать: 1 2 или 3? '))
        if hmm == 1:
            print(note1)
        elif hmm == 2:
            print(note2)
        elif hmm == 3:
            print(note3)
        else:
            print('это не число либо не 1 2 или 3')
        comand = input('введите следующую команду: ')
    elif comand == 'создание заметки':
        print('вам можно написать 3 заметки')
        hmmm = int(input('в какую хотите записать: 1 2 или 3? '))
        if hmmm == 1:
            note1 = input('')
        elif hmmm == 2:
            note2 = input('')
        elif hmmm == 3:
            note3 = input('')
        else:
            print('это не число либо не 1 2 или 3')
        comand = input('введите следующую команду: ')
    elif comand == 'запомнить контакт':
        name = input('ваше имя: ')
        secondname = input('ваша фамилия: ')
        noname = input('ваше отчество: ')
        number = int(input('ваш номер телевона: '))
        comand = input('введите следующую команду: ')
    elif comand == 'prize':
        while True:
            time.sleep(0.25)
            pyautogui.confirm(text = "IS'S TIME TO BE A [BIG SHOT!]", title = "SPAMTON G. SPAMTON", buttons = ["DEAL", "DEAL"])
    else:
        comand = input('повторите команду: ')

#после выхода
print('удачи')
exit
        
    