import functools # pragma: no cover

def decorator(func): # pragma: no cover
    @functools.wraps(func) # pragma: no cover
    def inner(*args, **kwargs): # pragma: no cover
        print('Decorator is called.') # pragma: no cover
        return func(*args, **kwargs) # pragma: no cover
    return inner # pragma: no cover

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

