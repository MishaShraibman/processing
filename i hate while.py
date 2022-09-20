import random

a = int(input("угадай число 1-100: "))
b = random.randint(1, 9)
while a != b:
    a = input(" ")
print("верно, а теперь иди в свою писочницу мелкишь")