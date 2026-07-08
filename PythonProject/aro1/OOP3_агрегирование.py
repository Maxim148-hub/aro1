class People:

    def __init__(self, name, age):
        self.__name = name

        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    def __str__(self):
        return f'{self.__name} - {self.__age}'

    def display(self):
        # mx = 0

        # for p in self.people:

        #     if len(p.name) > mx:

        #         mx = len(p.name)

        mx_obj = max(self.people, key=lambda p: len(p.name))

        mx = len(mx_obj.name)

        print(self)

        for n, p in enumerate(self.people, 1):
            print(f'{n}. {p.name:{mx}} - {p.age}')

        print()

    def __str__(self):
        return f'Квартира №{self.__number}'


class Floor:

    def __init__(self, numb):


p1 = People('Klava Koka', 30)

p2 = People('Said ibn Hattab', 80)

p3 = People('Jhone', 32)

p4 = People('Pol Maccartney', 70)

kv45 = Flat(45)

kv46 = Flat(46)

# print(kv45)

kv45.add_people(p1, p3)

kv46.add_people(p2, p4)

kv45.display()

kv46.display()