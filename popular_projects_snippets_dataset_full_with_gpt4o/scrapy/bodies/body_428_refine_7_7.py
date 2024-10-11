from twisted.python import failure # pragma: no cover

iterable = [1, 2, 3] # pragma: no cover
errback = lambda *args, **kwargs: print('Error callback', args, kwargs) # pragma: no cover
a = () # pragma: no cover
kw = {} # pragma: no cover
type('Mock', (object,), {'Failure': failure.Failure}) # pragma: no cover

from twisted.python import failure # pragma: no cover

iterable = [1, 2, None, 3] # pragma: no cover
def errback(f, *args, **kwargs): print(f'Error: {f}, args: {args}, kwargs: {kwargs}') # pragma: no cover
a = ('arg1', 'arg2') # pragma: no cover
kw = {'key1': 'value1'} # pragma: no cover
failure = type('MockFailure', (object,), {'Failure': failure.Failure}) # pragma: no cover

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
