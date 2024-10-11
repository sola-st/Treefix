from twisted.python import failure # pragma: no cover

iterable = [1, 2, 'stop', 4] # pragma: no cover
class MockFailure: # pragma: no cover
    def __init__(self, *args, **kwargs): # pragma: no cover
        self.args = args # pragma: no cover
        self.kwargs = kwargs # pragma: no cover
    def __str__(self): # pragma: no cover
        return f'MockFailure(args={self.args}, kwargs={self.kwargs})' # pragma: no cover
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
