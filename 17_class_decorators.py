''' Create a class decorator add_greeting that modifies a class to add a greet() method returning 
    "Hello from Decorator!". Apply it to a class Person.'''

def add_greeting(cls):
    def greet(self) -> str:
        return 'Hello from Decorator!'
    
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name: str) -> None:
        self.name = name

y1: Person = Person('Bilal')
print(y1.greet())