while True:
    first_num = int(input('Enter your first number: '))
    second_num = int(input('Enter your second number: '))
    operator = input('Enter your operator: ')

    if operator == '+':
        result = first_num + second_num
        print(f'{first_num} {operator} {second_num} = {result}')

    elif operator == '-':
        result = first_num - second_num
        print(f'{first_num} {operator} {second_num} = {result}')

    elif operator == '*':
        result = first_num * second_num
        print(f'{first_num} {operator} {second_num} = {result}')

    elif operator == '/':
        result = first_num / second_num
        print(f'{first_num} {operator} {second_num} = {result}')

    else:
        print(f'Your operator -> {operator} is invalid, we support only +, -, *, /')
    print()

    x = input('Do you wish to continue? y / n : ')

    if x == 'n':
        print()
        break
print('Thanks for playing!')