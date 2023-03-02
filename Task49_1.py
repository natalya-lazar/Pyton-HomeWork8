# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

def print_records(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            print(*line.split(';'))


def input_records(file_name: str):
    with open(file_name, 'r+', encoding='utf-8') as data:
        record_id = 0
        for line in data:
            if line != '':
                record_id = line.split(';')[:4][0]
        print('Введите фамилию, имя, отчество, номер телефона через пробел')
        line = f'{int(record_id) + 1};' + ';'.join(input().split()[:4]) + ';\n'
        data.write(line)


def find_records(file_name: str):
    print('По какой характеристике искать?')
    print('1 - фамилия, 2 - имя, 3 - отчество, 4 - номер')
    characteristic = input()
    while characteristic not in ['1', '2', '3', '4']:
        print('Введены неверные данные')
        print('По какой характеристике искать?')
        print('1 - фамилия, 2 - имя, 3 - отчество, 4 - номер')
        characteristic = input()
    condition = input('Введите поисковое значение\n')
    printed = False
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            if condition == line.split(';')[int(characteristic)]:
                print(*line.split(';'))
                printed = True
    if not printed:
        print("Не найдено")


path = 'phone_book.txt'

action = None
while action != 'q':
    action = input('Какое действие хотите совершить? 1 - чтение, 2 - запись. 3 - поиск, q - выход\n')
    while action not in ['1', '2', '3', 'q']:
        action = input('Какое действие хотите совершить? 1 - чтение, 2 - запись. 3 - поиск, q - выход\n')
        if action not in ['1', '2', '3', 'q']:
            print('Введены неверные данные')
    if action != 'q':
        if action == '1':
            print_records(path)
        elif action == '2':
            input_records(path)
        else:
            find_records(path)
            