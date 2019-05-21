class Cat():
    species = 'mammal'

    def __init__(self,breed, name='Lisa'):
        self.breed = breed
        self.name = name

mycat = Cat('Ben')



########  Наследование, инкапсуляция, подиморфизм

class Vehicle():
    def __init__(self, weight):
        print('Vehicle class created')
        self.weight = weight
        self.number_wheels = 4

    def _mytype(self):
        print('Type Vehicle')

vehicle = Vehicle(1000)
vehicle._mytype()

class Car(Vehicle):
    def __init__(self, weight):
        Vehicle.__init__(self, weight)
        print('Car class created!')
        self.number_doors = 4

    def car_name(self):
        print('Audi')

    def _mytype(self):
        print('Type Car')
car = Car(1500)
car.car_name()
car._mytype()
print(car.number_wheels, car.number_doors)

print('\n')

print('1' + '1')

print('\n')

class book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str___(self):
        return 'Title: {}, Author: {}, pages: {}'.format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book is destroyed')

b = book('Python', 'Jose', '200')
print(b)
# del b
