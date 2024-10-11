from twisted.python import failure # pragma: no cover

iterable = [1, 2, 3] # pragma: no cover
def errback(fail, *args, **kwargs): print('Error occurred:', fail) # pragma: no cover
failure = type('Mock', (object,), {'Failure': lambda: 'Mock Failure'})() # pragma: no cover
a = [] # pragma: no cover
kw = {} # pragma: no cover

from twisted.python import failure # pragma: no cover

iterable = [1, 2, 3, 'trigger error'] # pragma: no cover
def errback(failure_instance, *args, **kwargs): print('Error occurred:', failure_instance, args, kwargs) # pragma: no cover
class MockFailure: pass # pragma: no cover
failure = type('MockFailure', (object,), {'Failure': lambda: 'Mocked Failure'})() # pragma: no cover
a = ['arg1', 'arg2'] # pragma: no cover
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
