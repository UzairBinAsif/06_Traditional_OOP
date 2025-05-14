''' Write a decorator function log_function_call that prints "Function is being called" before a function 
    executes. Apply it to a function say_hello().'''

def log_function_call(func):
    
    def wrapping_func() -> None:
        print('Function is being called')
        return func()
    
    return wrapping_func

#                      func
# log_function_call(say_hello())

@log_function_call
def say_hello() -> None:
    print('Hello')

say_hello()