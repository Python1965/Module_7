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
#     filetime = ?
#     formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#     filesize = ?
#     parent_dir = ?
#     print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
# ****************************************************************************************

import os.path
import time

def file_info():

    for dirpath, dirnames, filenames in os.walk('.'):
        print(f'Найден каталог: {dirpath}')
        print(f'Список поддиректорий {dirnames}')
        
        for filename in filenames:
            print(f'Найден файл: {filename}')
            filepath = ?
            filetime = ?
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = ?
            parent_dir = ?
            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')



def start():
    file_info()

if __name__ == '__main__':
    start()