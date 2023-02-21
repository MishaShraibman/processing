import random
import time


place = [['O','T','O','O','O','O'],
         ['O','O','O','O','T','O',],
         ['T','O','T','O','O','O',],
         ['O','O','O','O','O','O',],
         ['O','O','O','T','O','O',],
         ['O','O','O','O','O','T',]]

place2 = [['I','O','I','O','O','O'],
          ['O','O','O','O','O','I',],
          ['I','O','I','O','O','O',],
          ['I','O','O','O','O','O',],
          ['O','O','O','I','O','O',],
          ['O','O','O','O','O','O',]]

bot_choice = [0,1,2,3,4,5]

X1 = 0
Y1 = 0

X2 = 0
Y2 = 0

type_start = input()

while type_start != 'выход':
    while ('T' in place[0] or 'T' in place[1] or 'T' in place[2] or 'T' in place[3] or 'T' in place[4] or 'T' in place[5]) and ('I' in place2[0] or 'I' in place2[1] or 'I' in place2[2] or 'I' in place2[3] or 'I' in place2[4] or 'I' in place2[5]):
    
        print('у каждого по x кораблей')

        Y2 = input()
        X2 = input()
        
        if Y2 == 'таблица' or X2 == 'таблица':
            for i in place:
                for y in i:
                    print(y,end='')
                print()
            Y2 = int(input())
            X2 = int(input())
            
        else:
            if X2 >= 6 or Y2 >= 6:
                print('не братан, за полем ставить незя')
        
            elif X2 <= -1 or Y2 <= -1:
                print('не братан, за поле не выходи то')
            else:
                if place2[Y2][X2] == 'I':
                    print('поподание!')
                    place2[Y2][X2] = 'X'
                    print(place2)
                else:
                    place2[Y2][X2] = '0'
                
        time.sleep(1)      
        print('следующий игрок')
        time.sleep(2)
        
        Y1 = random.choice(bot_choice)
        print(Y1)
        time.sleep(0.5)
        X1 = random.choice(bot_choice)
        print(X1)
        time.sleep(0.5)
        
        time.sleep(1)
    
        if X1 >= 6 or Y1 >= 6:
            print('не братан, за полем ставить незя')
        
        elif X1 <= -1 or Y1 <= -1:
            print('не братан, за поле не выходи то')
        else:
            if place[Y1][X1] == 'T':
                place[Y1][X1] = 'X'
                print("поподание!")
            else:
                place[Y1][X1] = '0'
    
        X1 = 0
        Y1 = 0
        X2 = 0
        Y2 = 0
        
        time.sleep(1)
        print("следующий игрок")
        time.sleep(2)
        
    print("игра окончена")
    time.sleep(1)
    type_start = input("сыграть ещё раз? ")
        

        
        