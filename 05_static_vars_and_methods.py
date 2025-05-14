''' Create a class MathUtils with a static method add(a, b) that returns the sum. 
    No class or instance variables should be used. '''
class MathUtils:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

result = MathUtils.add(2, 4)
print(result)