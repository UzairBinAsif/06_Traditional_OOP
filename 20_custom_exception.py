''' Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception
if age < 18. Handle it with try...except.'''

class InvalidAgeError(Exception):
    pass

def check_age(age) -> None:
    if age < 18:
        raise InvalidAgeError('You must be 18+')
    else:
        print('You\'re good to go.')

try:
    x: int = int(input('Enter your age: '))
    check_age(x)
except InvalidAgeError as i:
    print('Error:', i)