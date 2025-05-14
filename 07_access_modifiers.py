''' Create a class Employee with:
-> a public variable name,
-> a protected variable _salary, and
-> a private variable __ssn.
Try accessing all three variables from an object of the class and document what happens. '''

class Employee:
    def __init__(self, name: str, salary: int, ssn: int):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

e1 = Employee('Rehman', 1200, 1.2)
print(e1.name)    # public
print(e1._salary) # protected

# print(e1._Employee__ssn) # name mangling texhnique of accessing

try:
    print(e1.__ssn)   # private
except Exception as e:
    print('Error:', e)