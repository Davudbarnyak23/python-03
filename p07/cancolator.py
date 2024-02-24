print("canculator")
is_run = True

while is_run:
    print('actions:"+" "-" "*" "/" "^" exit: "x" ')
    number1 = float(input("num1?: "))
    number2 = float(input("num2?: "))
    action = input('action: ')

    if action == "x":
        is_run = False
    elif action == "+":
        result = number1 + number2
    elif action == "-":
        result = number1 - number2
    elif action == "*":
        result = number1 * number2
    elif action == "/":
        result = number1 / number2
    elif action == "^":
        result = number1 ^ number2
    else:
        print("error")
    print(result)
