''' Create a class Logger that prints a message when an object is created (constructor)
    and another message when it is destroyed (destructor). '''
    
class Logger:
    def __init__(self):
        print('Object created!')
    
    def __del__(self):
        print('Object destroyed!')
        

o1 = Logger()
del o1