''' Create a class Product with a private attribute _price. Use @property to get the price, @price.setter 
    to update it, and @price.deleter to delete it.'''

class Product:
    def __init__(self, price: int | float) -> None:
        self._price = price

    @property
    def price(self) -> int | float:
        return self._price
    
    @price.setter
    def price(self, amount: int | float) -> None:
        self._price = amount
    
    @price.deleter
    def price(self):
        del self._price

product1 = Product(2300)
print(product1.price)

product1.price = 1500
print(product1.price)

del product1.price

try:
    product1.price
except Exception as e:
    print('Error:', e)