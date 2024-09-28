# Домашнее задание по теме "Файлы в операционной системе".
# ***************************************************************************************
# Создайте новый проект или продолжите работу в текущем проекте.
#   - Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
#   - Примените os.path.join для формирования полного пути к файлам.
#   - Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
#   - Используйте os.path.getsize для получения размера файла.
#   - Используйте os.path.dirname для получения родительской директории файла.
#
# Комментарии к заданию:#
# Ключевая идея – использование вложенного for:
#
# for root, dirs, files in os.walk(directory):
#   for file in files:
#     filepath = ?
#     filetime =
#     formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#     filesize = ?
#     parent_dir = ?
#     print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
# ****************************************************************************************

import os
import time


def file_info(cur_dir):

    for dirpath, dirnames, filenames in os.walk(cur_dir):
        print()
        print(f'Текущий каталог: {os.path.abspath(dirpath)}')
        print(f'Список подкаталогов: {dirnames}')

        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            filetime = os.path.getmtime(filepath)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(filepath)
            parent_dir = dirpath
            print(f'    Найден файл: {filename}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

        for dirname in dirnames:
            new_dir = os.path.join(cur_dir, dirname.replace('.', "", 1))
            file_info(new_dir)


def cat_stru_printing():
    work_dir = os.getcwd()
    print(f'Рабочий каталог: {work_dir}')
    file_info(work_dir)


def start():
    cat_stru_printing()

if __name__ == '__main__':
    start()