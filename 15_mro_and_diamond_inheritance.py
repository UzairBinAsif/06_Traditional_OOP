#  METHOD RESOLUTION ORDER -> MRO
''' Create four classes:
A with a method show(),
B and C that inherit from A and override show(),
D that inherits from both B and C.
Create an object of D and call show() to observe MRO.'''

class A:
    def show(self):
        print('Content of A')

class B(A):
    def show(self):
        print('Content of B')

class C(A):
    def show(self):
        print('Content of C')

class D(B, C):
    pass

obj1 = D()
obj1.show()