import asyncio # pragma: no cover
from twisted.python.failure import Failure # pragma: no cover

class MockAIterable: # pragma: no cover
    def __init__(self, with_error=False): # pragma: no cover
        self.with_error = with_error # pragma: no cover
        self.counter = 0 # pragma: no cover
 # pragma: no cover
    def __aiter__(self): # pragma: no cover
        return self # pragma: no cover
 # pragma: no cover
    async def __anext__(self): # pragma: no cover
        if self.with_error or self.counter >= 1: # pragma: no cover
            raise Exception('Test exception') # pragma: no cover
        self.counter += 1 # pragma: no cover
        return 'test_value' # pragma: no cover
 # pragma: no cover
def errback(failure_instance, *args, **kwargs): # pragma: no cover
    print(f'Error callback executed: {failure_instance}') # pragma: no cover
 # pragma: no cover
aiterable = MockAIterable(with_error=True) # pragma: no cover
a = [] # pragma: no cover
kw = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
from l3.Runtime import _l_
"""Wraps an async iterable calling an errback if an error is caught while
    iterating it. Similar to scrapy.utils.defer.iter_errback()
    """
it = aiterable.__aiter__()
_l_(20139)
while True:
    _l_(20146)

    try:
        _l_(20145)

        aux = await it.__anext__()
        _l_(20140)
        exit(aux)
    except StopAsyncIteration:
        _l_(20142)

        break
        _l_(20141)
    except Exception:
        _l_(20144)

        errback(failure.Failure(), *a, **kw)
        _l_(20143)
