''' Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make 
    the object iterable in a for-loop, counting down to 0.'''

class Countdown:
    def __init__(self, start_num: int) -> None:
        self.current_num: int = start_num 
    
    def __iter__(self):
        return self
    
    def __next__(self) -> int | Exception:
        if self.current_num <= 0:
            raise StopIteration
        else:
            num = self.current_num
            self.current_num -= 1
            return self.current_num

my_iterator: Countdown = Countdown(10)

for i in my_iterator:
    print(i+1)