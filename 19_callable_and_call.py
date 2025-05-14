''' Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an 
    input by the factor. Test it with callable() and by calling the object like a function.'''

class Multiplier:
    def __init__(self, factor: int) -> None:
        self.factor: int = factor

    def __call__(self, user_input: int) -> int:
        self.user_input: int = user_input
        return self.user_input * self.factor

m1: Multiplier = Multiplier(3)

print(m1.__call__(7))
print(callable(m1))
print(m1(4))