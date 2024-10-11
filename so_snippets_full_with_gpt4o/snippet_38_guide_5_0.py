from functools import wraps # pragma: no cover

def decorator(f): # pragma: no cover
    @wraps(f) # pragma: no cover
    def wrapper(*args, **kwargs): # pragma: no cover
        print('Decorator executed') # pragma: no cover
        return f(*args, **kwargs) # pragma: no cover
    return wrapper # pragma: no cover
def func(): # pragma: no cover
    print('Function originally defined') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/739654/how-do-i-make-function-decorators-and-chain-them-together
from l3.Runtime import _l_
@decorator
def func():
    _l_(13405)

    ...
    _l_(13404)

def func():
    _l_(13407)

    ...
    _l_(13406)
func = decorator(func)
_l_(13408)

