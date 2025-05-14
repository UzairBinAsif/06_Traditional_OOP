''' Create a class Person with a constructor that sets the name. Inherit a class Teacher from it,
    add a subject field, and use super() to call the base class constructor.'''

class Person:
    def __init__(self, name: str):
        self.name = name

class Teacher(Person):
    def __init__(self, name: str, subject: str):
        super().__init__(name)
        self.subject = subject

teacher1 = Teacher('ali', 'python')
print(f'Our Teacher\'s name is {teacher1.name}, He Teaches us {teacher1.subject}.')