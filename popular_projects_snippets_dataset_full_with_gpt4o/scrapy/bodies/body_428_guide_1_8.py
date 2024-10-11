from twisted.python import failure # pragma: no cover

iterable = [1, 'error', 3] # pragma: no cover
class MockFailure: # pragma: no cover
    def __init__(self, exc_info=None): # pragma: no cover
        self.exc_info = exc_info # pragma: no cover
 # pragma: no cover
    def __str__(self): # pragma: no cover
        return f'MockFailure({self.exc_info})' # pragma: no cover
 # pragma: no cover
def errback(failure, *a, **kw): # pragma: no cover
    print(f'Error caught: {failure}') # pragma: no cover
 # pragma: no cover
    if value == 'error': # pragma: no cover
        raise ValueError('An error occurred') # pragma: no cover
    print(value) # pragma: no cover
 # pragma: no cover
a = [] # pragma: no cover
kw = [] # pragma: no cover
failure.Failure = MockFailure # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
from l3.Runtime import _l_
"""Wraps an iterable calling an errback if an error is caught while
    iterating it.
    """
it = iter(iterable)
_l_(16107)
while True:
    _l_(16114)

    try:
        _l_(16113)

        aux = next(it)
        _l_(16108)
        exit(aux)
    except StopIteration:
        _l_(16110)

        break
        _l_(16109)
    except Exception:
        _l_(16112)

        errback(failure.Failure(), *a, **kw)
        _l_(16111)
