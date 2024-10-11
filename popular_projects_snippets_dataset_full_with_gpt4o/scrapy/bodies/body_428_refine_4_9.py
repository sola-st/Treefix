from itertools import cycle # pragma: no cover

iterable = cycle([1, 2, 3]) # pragma: no cover
errback = lambda exc, *args, **kwargs: print(f"Error: {exc}") # pragma: no cover
failure = type('FailureMock', (object,), {'Failure': lambda: 'failure_instance'}) # pragma: no cover
a = ('arg1', 'arg2') # pragma: no cover
kw = {'key1': 'value1', 'key2': 'value2'} # pragma: no cover

iterable = [1, 'a', None, 4] # pragma: no cover
def errback(failure_obj, *args, **kwargs): print(f"Error handled: {failure_obj}", args, kwargs) # pragma: no cover
class MockFailure:# pragma: no cover
    @staticmethod# pragma: no cover
    def Failure(): return 'Mocked Failure'# pragma: no cover
failure = MockFailure() # pragma: no cover
a = ('extra arg1', 'extra arg2') # pragma: no cover
kw = {'key1': 'value1', 'key2': 'value2'} # pragma: no cover

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
