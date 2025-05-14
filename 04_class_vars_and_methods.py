''' Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name)
    that allows changing the bank name. Show that it affects all instances.'''

class Bank:
    bank_name = 'HBL'
    
    def __init__(self):
        pass
    
    @classmethod
    def change_bank_name(cls, name: str) -> None:
        Bank.bank_name = name

bank1 = Bank()
bank2 = Bank()

print(f'Bank1\'s name before: {bank1.bank_name}')
print(f'Bank2\'s name before: {bank2.bank_name}')

Bank.change_bank_name('Al Habib')

print(f'Bank1\'s name after: {bank1.bank_name}')
print(f'Bank2\'s name after: {bank2.bank_name}')