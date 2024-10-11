import sys # pragma: no cover
from twisted.python import failure # pragma: no cover

iterable = [1, 2, 3, 4, 5] # pragma: no cover
def errback(exc, *args, **kwargs): print('Error caught:', exc, args, kwargs) # pragma: no cover
failure = type('MockFailure', (object,), {'Failure': lambda: 'Mocked Failure'}) # pragma: no cover
a = ['arg1', 'arg2'] # pragma: no cover
kw = {'key1': 'value1', 'key2': 'value2'} # pragma: no cover

from twisted.python import failure # pragma: no cover

iterable = iter([1, 2, 3]) # pragma: no cover
def errback(exc, *args, **kwargs): print('Error caught:', exc, args, kwargs) # pragma: no cover
def mock_failure(): return 'Mocked Failure' # pragma: no cover
failure = type('MockFailure', (object,), {'Failure': mock_failure})() # pragma: no cover
a = (10, 20) # pragma: no cover
kw = {'key': 'value'} # pragma: no cover

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
