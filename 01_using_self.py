''' Create a class Student with attributes name and marks. Use the self keyword to initialize these
    values via a constructor. Add a method display() that prints student details.'''

class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks
    def display(self):
        print(f'The student\'s name is {self.name} and his marks are {self.marks}')

s1 = Student('Uzair', 63)
s1.display()