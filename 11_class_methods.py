''' Create a class Book with a class variable total_books. Add a class method increment_book_count()
    to increase the count when a new book is added.'''

class Book:
    total_books: int = 0
    def __init__(self, name: str) -> None:
        self.name = name
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls) -> None:
        cls.total_books += 1
    

b1 = Book('Stranger Things')
b2 = Book('Jujutsu Kaisen')
b2 = Book('Kung fu Panda')

print('Total Books:', Book.total_books)