# Домашнее задание по теме "Оператор "with".
# ***************************************************************************************
#  Задача "Найдёт везде":
# Напишите класс WordsFinder, объекты которого создаются следующим образом:
# WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
#   Объект этого класса должен принимать при создании неограниченного количество названий файлов
#   и записывать их в атрибут file_names в виде списка или кортежа.
#
# Также объект класса WordsFinder должен обладать следующими методами:
#   - get_all_words - подготовительный метод, который возвращает словарь следующего вида:
#     {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
#       Где:
#         'file1.txt', 'file2.txt', "file3.txt" - названия файлов.
#         ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
#       Алгоритм получения словаря такого вида в методе get_all_words:
#         - Создайте пустой словарь all_words.
#         - Переберите названия файлов и открывайте каждый из них, используя оператор with.
#         - Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
#         - Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке.
#           (тире обособлено пробелами, это не дефис в слове).
#         - Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
#         - В словарь all_words запишите полученные данные, ключ - название файла, значение - список
#           из слов этого файла.
#
#   - find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
#     значение - позиция первого такого слова в списке слов этого файла.
#   - count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
#     значение - количество слова word в списке слов этого файла.
#
#   В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла
#   и списка его слов.
#   Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом
#   словаря - item().
#
#   # for name, words in get_all_words().items():
#   # Логика методов find или count
#
# ****************************************************************************************

import os.path

class WordsFinder:

    def __init__(self, *files):
        self.file_names = []

        for item in files:
            if isinstance(item , str):
                self.file_names.append(item)

            if isinstance(item, dict):
                for key in item.keys():
                    self.file_names.append(key)
                    if os.path.isfile(key):
                        os.remove(key)

                    with open(key, "w", encoding='utf-8') as file:
                        for val in item.values():
                            for val_ in val:
                                file.write(f"{val_}\n")

    def get_all_words(self):
        dict_ = {}
        subst_list = [",", '.', '=', '!', '?', ';', ':', ' - ']

        for key in self.file_names:
            str_ = ""
            with open(key, 'r', encoding='utf-8') as file:
                for line in file:
                    line_ = line.rstrip()
                    for item_ in subst_list:
                        line_ = line_.replace(item_, " ")

                    str_ += " " + line_.lower()
                str_ = str_.replace(' ', "", 1)

                dict_[key] = str_.split()

        return dict_

    def find(self, word):
        dic_main = self.get_all_words()

        word = word.lower()
        for key, values in dic_main.items():
            i = 0
            for val in values:
                i += 1
                if val == word:
                    return {key: i}

            return None

    def count(self, word):
        dic_main = self.get_all_words()

        word = word.lower()
        for key, values in dic_main.items():
            i = 0
            for val in values:
                if val == word:
                    i += 1

            if i > 0: return {key: i}

        return None


def start():
    dic_1 = {"test_file.txt": ["It's a text for task Найти везде,",
                               "Используйте его для самопроверки.",
                               "Успехов в решении задачи!",
                               "text text text"]}

    finder1 = WordsFinder(dic_1)
    finder1.get_all_words()
    print(finder1.get_all_words())  # Все слова
    print(finder1.find('TEXT'))   # 3 слово по счёту
    print(finder1.count('teXT'))  # 4 слова teXT в тексте всего

    #inder2 = WordsFinder('test_file.txt')
    # print(finder2.get_all_words())  # Все слова
    # print(finder2.find('TEXT'))  # 3 слово по счёту
    # print(finder2.count('teXT'))  # 4 слова teXT в тексте всего


if __name__ == '__main__':
    start()