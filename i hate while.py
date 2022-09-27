import random

a = int(input("угадай число 1-100: "))
b = random.randint(1, 100)
while a != b:
    a = int(input(" "))
print("верно, а теперь иди читер грёбаный")
