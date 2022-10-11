import random
alisa = input('здравствуйте, чем могу помочь? ')
anekdot = ['появился как то в зоне чёрный сталкер','пришёл как то мужик квартиру покупать']
shutka = ['партия','решил как то безногий прогуляться']
dom = ['na na na na n ana na na nna na ananna nane enen nenenononnnoo','включаю смачное приготовление пельменей']
school = ["пошёл в школу кожанное существо",'ты кто?']
while alisa != "пока":
    num = random.randint(1,100)
    if alisa == "анекдот":
        print(random.choice(anekdot))
        alisa = input("что ещё? ")
    elif alisa == 'шутка':
        print(random.choice(shutka))
        alisa = input('что ещё? ')
    elif alisa == 'алиса, я дома':
        if num >= 0 and num <= 10:
            print(random.choice(dom))
            alisa = input('что ещё? ')
        else:
            print('добро пожаловать')
            alisa = input('что ещё? ')
    elif alisa == 'алиса, доброе утро':
        if num >= 6 and num <= 25:
            print(random.choice(school))
            alisa = input('что ещё? ')
        elif num >= 0 and num <= 5:
            print('im 27 years old man with dementia, and actually 27 years old man with dementia...')
            alisa = input('что ещё? ')
        else:
            print('и вам доброе утро')
            alisa = input('что ещё? ')
    else:
        print('не расслышала')
        alisa = input('что ещё? ')
print("до встречи")
