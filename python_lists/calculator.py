first_num = int(input('Enter your first number: '))
second_num = int(input('Enter your second number: '))
operator = input('Enter your operator: ')

print(f'{first_num} {operator} {second_num} = x')

if operator == '+':
    result = first_num + second_num
    print(f'{first_num} {operator} {second_num} = {result}')
