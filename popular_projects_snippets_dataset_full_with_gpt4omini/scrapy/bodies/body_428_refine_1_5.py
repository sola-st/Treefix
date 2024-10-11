from twisted.python import failure # pragma: no cover

iterable = [1, 2, 3] # pragma: no cover
def errback(failure, *args, **kwargs): print('An error occurred:', failure, args, kwargs) # pragma: no cover
failure = type('MockFailure', (object,), {'Failure': lambda: 'Mocked failure'}) # pragma: no cover
a = (10, 20) # pragma: no cover
kw = {'key': 'value'} # pragma: no cover

from twisted.python import failure # pragma: no cover

iterable = [1, 2, 3] # pragma: no cover
def errback(failure_instance, *args, **kwargs): print('An error occurred:', failure_instance, args, kwargs) # pragma: no cover
class MockFailure: pass # pragma: no cover
failure = type('FailureMock', (object,), {'Failure': MockFailure})() # pragma: no cover
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
