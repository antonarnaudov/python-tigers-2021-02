def print_result(num1, operator, num2, result):
    return print(f'{num1} {operator} {num2} = {result}')


def sum_nums(num1, num2):
    return num1 + num2


first_num = int(input('Enter your first number: '))
second_num = int(input('Enter your second number: '))
operator = input('Enter your operator: ')

if operator == '+':
    result = sum_nums(first_num, second_num)
    print_result(first_num, operator, second_num, result)

elif operator == '-':
    result = first_num - second_num
    print_result(first_num, operator, second_num, result)

elif operator == '*':
    result = first_num * second_num
    print_result(first_num, operator, second_num, result)

elif operator == '/':
    result = first_num / second_num
    print_result(first_num, operator, second_num, result)

else:
    print(f'Your operator -> {operator} is invalid, we support only +, -, *, /')
