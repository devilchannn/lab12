from tkinter import *


def lab1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название ресторана: {self.restaurant_name}, кухня: {self.cuisine_type} ')

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors, location, open):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors
            self.location = location
            self.open = open

        def describe_rest(self):
            print(f'Адрес ресторана: {self.location}, часы работы ресторана {self.open}')


        def add_flavors(self):
            f.append(input('Какие вкусы добавить? '))

        def del_flavors(self):
            f.remove(input('Какие вкусы убрать? '))

        def vflavors(self):
            print('Список сортов мороженного: ', n)

        def check(self):
            if str(input('Какой сорт вам нужен? ')) in n:
                print('Такой есть')
            else:
                print('Такого нет')

    f = ['Шоколадное', 'Ванильное', 'Черничное', 'Клубничное']

    n = ['Эскимо', 'Щербет', 'Сладкий лед']

    r = IceCreamStand('PENGUINS', 'итальянская', f, 'ул. Счастья 20 ', '10:00 - 18:00')

    r.describe_restaurant()
    r.describe_rest()
    r.add_flavors()
    r.del_flavors()
    r.vflavors()