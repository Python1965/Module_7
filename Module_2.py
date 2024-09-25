# Домашнее задание по теме "Позиционирование в файле".
# ***************************************************************************************
#  Задача "Записать и запомнить":
# Создайте функцию custom_write(file_name, strings), которая принимает аргументы
#   - file_name - название файла для записи,
#   - strings - список строк для записи.
#
# Функция должна:
#   - Записывать в файл file_name все строки из списка strings, каждая на новой строке.
#   - Возвращать словарь strings_positions, где ключом будет кортеж
#     (<номер строки>, <байт начала строки>), а значением - записываемая строка.
#     Для получения номера байта начала строки используйте метод tell() перед записью.
#
# Пример полученного словаря:
#  {(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
#   Где:
#       1, 2 - номера записанных строк.
#       0, 16 - номера байт, на которых началась запись строк.
#   'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.
#
# ****************************************************************************************

import os.path

def custom_write(file_name, strings):

    strings_positions = {}

    if len(strings) > 0:

        if not os.path.isfile(file_name):
            file = open(file_name, "x", encoding='utf-8')
            file.close()
            lines = 0

        else:
            with open(file_name, 'r', encoding='utf-8') as file:
                lines = sum(1 for line in file)

        line_ = lines
        with open(file_name, 'a+', encoding='utf-8') as file:
            for item in strings:
                line_ += 1
                start_byte = file.tell()
                file.write(f"{item}\n")
                strings_positions[(line_, start_byte)] = item

    return strings_positions


def start():

    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
        

if __name__ == '__main__':
    start()