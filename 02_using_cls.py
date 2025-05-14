''' Create a class Counter that keeps track of how many objects have been created.
    Use a class variable and a class method with cls to manage and display the count.'''
    
class Counter:
    count: int = 0
    
    def __init__(self) -> None:
        Counter.count += 1
    
    @classmethod
    def show(cls) -> None:
        print('\nTotal objects created in memory =', cls.count)
        
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()

Counter.show()