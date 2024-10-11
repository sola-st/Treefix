from twisted.python import failure # pragma: no cover

iterable = [1, 2, 3] # pragma: no cover
errback = lambda *args, **kwargs: print('Error occurred', args, kwargs) # pragma: no cover
a = () # pragma: no cover
kw = {} # pragma: no cover
failure = type('MockFailure', (object,), {'Failure': lambda: 'Failure object'}) # pragma: no cover

from twisted.python.failure import Failure # pragma: no cover

iterable = [1, 2, 'error', 4] # pragma: no cover
def errback(f, *args, **kwargs):# pragma: no cover
    print(f"Error handled: {f}", args, kwargs) # pragma: no cover
class MockFailure:# pragma: no cover
    @staticmethod# pragma: no cover
    def Failure():# pragma: no cover
        try:# pragma: no cover
            raise ValueError('Mock error')# pragma: no cover
        except ValueError:# pragma: no cover
            return Failure()# pragma: no cover
failure = MockFailure # pragma: no cover
a = () # pragma: no cover
kw = {} # pragma: no cover

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
