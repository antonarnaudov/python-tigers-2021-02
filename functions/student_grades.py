# person_type = 'Student'
average_grades = 0

grades = []

student_name = input('Enter your name: ')


def again():
    try_again = input('Do you wish to continue? y/n -> ')
    # Можеш да изтриеш принта
    print(try_again)
    start()


def start():
    current_grade = int(input('Enter your grade: '))
    # Можеш да изтриеш принта
    print(current_grade)
    again()


start()

# 1
# again() --> да се напише проверка която проверява дали искаме да продължим или не

# 2
# start() --> да се напише код който проверява дали оценката е валидна тоест между 2-6
# и ако е валидна я добавя към листа grades,
# ако не е Принтира, че оценката не е валидна.

# 3
# При приключване на програмата, тоест след извикването на start() ->
# след 21 ред. Да се напише код който изчислява средната оценка.
# Сумата на листа grades делено на Дължината на листа grades.
# grades.sum() / grades.len()
