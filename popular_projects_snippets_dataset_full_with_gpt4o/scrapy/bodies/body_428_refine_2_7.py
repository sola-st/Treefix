import itertools # pragma: no cover
from unittest.mock import Mock # pragma: no cover

iterable = [1, 2, 3, 4] # pragma: no cover
def errback(failure, *a, **kw): print('Error:', failure, a, kw) # pragma: no cover
failure = type('Mock', (object,), {'Failure': Mock(return_value='mocked failure')}) # pragma: no cover
a = (1, 2) # pragma: no cover
kw = {'key': 'value'} # pragma: no cover

iterable = [1, 'a', 3.0] # pragma: no cover
def errback(failure, *a, **kw):# pragma: no cover
    print(f"Error: {failure}")# pragma: no cover
    print(f"Args: {a}")# pragma: no cover
    print(f"Kwargs: {kw}") # pragma: no cover
class MockFailure:# pragma: no cover
    def Failure(self):# pragma: no cover
        return "Mocked failure" # pragma: no cover
failure = MockFailure() # pragma: no cover
a = ('extra_arg1', 'extra_arg2') # pragma: no cover
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
