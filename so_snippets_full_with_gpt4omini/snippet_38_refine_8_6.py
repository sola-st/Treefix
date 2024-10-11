def decorator(func): # pragma: no cover
    @functools.wraps(func) # pragma: no cover
    def wrapper(): # pragma: no cover
        print('Decorator executed.') # pragma: no cover
        func() # pragma: no cover
    return wrapper # pragma: no cover

import functools # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/739654/how-do-i-make-function-decorators-and-chain-them-together
from l3.Runtime import _l_
@decorator
def func():
    _l_(1416)

    ...
    _l_(1415)

def func():
    _l_(1418)

    ...
    _l_(1417)
func = decorator(func)
_l_(1419)

