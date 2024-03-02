import random

# y = {'x': 222, 'y': 111, 'z': 12}
#
# for key, item in y:
#     print(key, ' = ', item)

# for k if random(1, 101)
#
#     print("вгадай число")
#     number1 = float(input("num1?: "))
#
#     if: k== number1
#         print(win)
#
#     elif: k > number1
#         print("номер більший за вказаний")
#
#     elif: k < number1
#         print("num min")

guess = random.randint(1,100)

while True:
    number = int(input('num:'))

    if guess == number:
        print('win')
        break
    elif guess > number:
        print('100')

    elif guess < number:
        print('00')