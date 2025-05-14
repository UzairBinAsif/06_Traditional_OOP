''' Create a class Car with a public variable brand and a public method start(). 
    Instantiate the class and access both from outside the class.'''

class Car:
    def __init__(self, brand: str):
        self.brand = brand
        
    def start(self) -> None:
        print(f'You {self.brand}, started :)')
    
car1 = Car('Mercedes')
print(f'Brand of car: {car1.brand}')
car1.start()