# Домашнее задание по теме "Режимы открытия файлов"
# ***************************************************************************************
#  Задача "Учёт товаров":
# Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться
# запись в файл с продуктами.
# Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables')
# и обладать следующими свойствами:
#   - Атрибут name - название продукта (строка).
#   - Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
#   = Атрибут category - категория товара (строка).
#   - Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
#     Все данные в строке разделены запятой с пробелами.
#
# Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
# Инкапсулированный атрибут
#   - __file_name = 'products.txt'.
#   - Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его
#     и возвращает единую строку со всеми товарами из файла __file_name.
#   - Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
#     Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
#     Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине'.
#
# Пример работы программы:
# s1 = Shop()
# p1 = Product('Potato', 50.5, 'Vegetables')
# p2 = Product('Spaghetti', 3.4, 'Groceries')
# p3 = Product('Potato', 5.5, 'Vegetables')
#
# print(p2) # __str__
#
# s1.add(p1, p2, p3)
#
# print(s1.get_products())
#
# ****************************************************************************************

import os.path

class Product:
    name = ''       # название продукта (строка).
    weight = 0      # общий вес товара (дробное число) (5.4, 52.8 и т.п.).
    category = ''   # категория товара (строка).

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    def add(self, *products):   # принимает неограниченное количество объектов класса Product.
                                # Добавляет в файл __file_name каждый продукт из products, если его ещё нет
                                # в файле (по названию). Если такой продукт уже есть, то не добавляет
                                # и выводит строку 'Продукт <название> уже есть в магазине'.

        products_ = list(products)

        if not os.path.isfile(self.__file_name):
            file = open(self.__file_name, "x")
            file.close()

        with open(self.__file_name, 'r', encoding='utf-8') as file:
            for line in file:
                for item in products:
                    if line == f"{item.name}, {item.weight}, {item.category}\n":
                        print(f"Продукт {item.name} уже есть в магазине")
                        products_.remove(item)
                        break
        file.close()

        if len(products_) > 0:
            file = open(self.__file_name, "a+", encoding='utf-8')
            for item in products_:
                file.write(f"{item.name}, {item.weight}, {item.category}\n")

            file.close()


    def get_products(self):     # считывает всю информацию из файла __file_name, закрывает его
                                # и возвращает единую строку со всеми товарами из файла __file_name.

        with open(self.__file_name, 'r', encoding='utf-8') as file:
            data = file.readlines()
            file.close()
        return data


def start():
    s1 = Shop()

    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p1)  # __str__
    print(p2)  # __str__
    print(p3)  # __str__

    s1.add(p1, p2)
    s1.add(p3)

    print(s1.get_products())


if __name__ == '__main__':
    start()