class Animal:

    def __init__(self, name, owner, color, speed):
        self.__name = name
        self.__owner = owner
        self.color = color
        self.speed = speed

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

cat_1 = Animal('Frosya', 'Dasha', 'multiple', 5)
cat_1.set_name('John')
# print(cat_1.get_name())
cat_1.owner = 'Jack'
# print(cat_1.owner)

class Cat(Animal):

    def __init__(self, name, owner, color, speed):
        self.name = name
        self.owner = owner
        super().__init__(name, owner, color, speed)

    def says(self, word):
        return f'Cat named {self.name} says {word}'


cat_2 = Cat('Pinky', 'Vasya', 'brown', 5)
print(cat_2.says('meow meow'))

class Dog(Animal):
    pass

dog_1 = Dog('Sam', 'Dima', 'red', 8)
print(dog_1.__dict__)
dog_1.__dict__ = {'_Animal__name': 'Sam', '_Animal__owner': 'Dima', 'color': 'red', 'speed': 8, 'type': 'mammal'}
print(dog_1.type)