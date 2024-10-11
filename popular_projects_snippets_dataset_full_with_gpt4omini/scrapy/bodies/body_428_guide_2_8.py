from collections.abc import Iterable # pragma: no cover
class MockFailure: # pragma: no cover
    def __init__(self): pass # pragma: no cover
def errback(f, *args, **kwargs): print('Error occurred:', f) # pragma: no cover

iterable = iter(['valid', 'data']) # pragma: no cover
def next(it): raise Exception('Simulated error') # pragma: no cover
a = [] # pragma: no cover
kw = {} # pragma: no cover
failure = MockFailure() # pragma: no cover

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
