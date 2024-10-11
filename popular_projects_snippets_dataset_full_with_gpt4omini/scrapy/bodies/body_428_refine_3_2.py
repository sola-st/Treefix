from typing import Callable, Any, Iterable, Type # pragma: no cover

iterable = [1, 2, 3, 4, 5] # pragma: no cover
def errback(*args: Any, **kwargs: Any): pass # pragma: no cover
class Mock: pass # pragma: no cover
failure = type('MockFailure', (object,), {'Failure': lambda: 'An error occurred'})() # pragma: no cover
a = [] # pragma: no cover
kw = {} # pragma: no cover

from twisted.python import failure # pragma: no cover

iterable = [1, 2, 3, 4, 5] # pragma: no cover
def errback(failure, *args, **kwargs): print('Error caught:', failure, args, kwargs) # pragma: no cover
class MockFailure: pass # pragma: no cover
failure = type('MockFailure', (object,), {'Failure': lambda self: 'Mocked failure occurred'})() # pragma: no cover
a = ['additional', 'parameters'] # pragma: no cover
kw = {'key1': 'value1', 'key2': 'value2'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
from l3.Runtime import _l_
"""Wraps an iterable calling an errback if an error is caught while
    iterating it.
    """
it = iter(iterable)
_l_(4520)
while True:
    _l_(4527)

    try:
        _l_(4526)

        aux = next(it)
        _l_(4521)
        exit(aux)
    except StopIteration:
        _l_(4523)

        break
        _l_(4522)
    except Exception:
        _l_(4525)

        errback(failure.Failure(), *a, **kw)
        _l_(4524)
