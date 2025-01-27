# Extracted from https://stackoverflow.com/questions/5929107/decorators-with-parameters
pip install pamda

@pamda.curry()
def my_decorator(input, func):
    print ("Executing Decorator")
    print(f"input:{input}")
    return func

@my_decorator('Hi!')
def foo(input):
    print('Executing Foo!')
    print(f"input:{input}")

x=foo('Bye!')

from pamda import pamda

@pamda.curry()
def my_decorator(input, func):
    print ("Executing Decorator")
    print(f"input:{input}")
    return func

@my_decorator('Hi!')
def foo(input):
    print('Executing Foo!')
    print(f"input:{input}")

x=foo('Bye!')

Executing Decorator
input:Hi!
Executing Foo!
input:Bye!

