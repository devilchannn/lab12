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
    r.check()

def lab2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, flavors, location, open):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.flavors = flavors
            self.location = location
            self.open = open

        def describe_rest(self):
            print(
                f'Название ресторана: {self.restaurant_name}, кухня: {self.cuisine_type}\nРасположение ресторана: {self.location}, часы работы ресторана {self.open} ')

        def flavors(self):
            print('Вкусы мороженного:', f)

    f = ['Шоколадное', 'Ванильное', 'Черничное', 'Клубничное']

    r = Restaurant('PENGUINS', 'итальянская', f, 'ул. Счастья 20 ', '10:00 - 18:00')
    r.describe_rest()

    i = Tk()
    i['backgr'] = 'salmon4'
    i.title('Вкусы')
    i.geometry('300x300')
    frame = Frame(i, bg='white smoke', bd=5)
    frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)
    title = Label(i, text='Вкусы мороженного:', bg='white smoke', font=30)
    title.place(relx=0.15, rely=-0.25, relwidth=0.7, relheight=0.7)
    title.pack

    ch = 0.1
    for k in f:
        e = k
        ch += 0.12
        m = Label(i, text=e, bg='white smoke', font=25)
        m.place(relx=0.15, rely=ch, relwidth=0.7, relheight=0.1)
        m.pack
    i.mainloop()

lab1()
lab2()