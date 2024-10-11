from twisted.python import failure # pragma: no cover

iterable = [1, 2, 'a', 4] # pragma: no cover
def errback(f, *a, **kw): print(f'Error: {f}, args: {a}, kwargs: {kw}') # pragma: no cover
class MockFailure:# pragma: no cover
    class Failure:# pragma: no cover
        def __init__(self):# pragma: no cover
            pass # pragma: no cover
a = ('example',) # pragma: no cover
kw = {'key1': 'value1'} # pragma: no cover

iterable = [1, 2, 3, 'error'] # pragma: no cover
def errback(failure_obj, *a, **kw): print(f"Error handled: {failure_obj}", a, kw) # pragma: no cover
class FailureMock:# pragma: no cover
    class Failure:# pragma: no cover
        def __init__(self):# pragma: no cover
            self.value = 'failure_instance'# pragma: no cover
        def __repr__(self):# pragma: no cover
            return self.value # pragma: no cover
failure = FailureMock() # pragma: no cover
a = ('arg1', 'arg2') # pragma: no cover
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
