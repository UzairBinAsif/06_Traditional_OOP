''' Use the abc module to create an abstract class Shape with an abstract method area().
    Inherit a class Rectangle that implements area().'''
    
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width
    
    def area(self) -> int:
        return self.length * self.width

area1 = Rectangle(2, 4)
print(f'Area is: {area1.area()}')
