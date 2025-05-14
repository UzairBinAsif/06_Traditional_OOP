''' Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class
    during initialization. Access a method of the Engine class via the Car class.'''

class Engine:
    def fuel_warning(self) -> None:
        print('Low Fuel!')

class Car:
    def __init__(self, engine: Engine) -> None:
        self.engine: Engine = engine

    def show_fuel_warning(self) -> None:
        self.engine.fuel_warning()


e1: Engine = Engine()
c1: Car = Car(e1)
c1.show_fuel_warning()