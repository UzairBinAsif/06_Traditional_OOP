''' Create a class Dog with instance variables name and breed. Add an instance method bark() 
    that prints a message including the dog's name.'''

class Dog:
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed
    
    def bark(self) -> None:
        print(f'My name is {self.name} the {self.breed}, Woof Woof!!!')

d1 = Dog('Rob', 'Rottweiler')
d1.bark()