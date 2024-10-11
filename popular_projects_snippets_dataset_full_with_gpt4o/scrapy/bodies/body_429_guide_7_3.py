import asyncio # pragma: no cover
from twisted.python.failure import Failure # pragma: no cover

class MockAIterable: # pragma: no cover
    def __init__(self, raise_exception_on_first=False): # pragma: no cover
        self.raise_exception_on_first = raise_exception_on_first # pragma: no cover
        self.counter = 0 # pragma: no cover
    def __aiter__(self): # pragma: no cover
        return self # pragma: no cover
    async def __anext__(self): # pragma: no cover
        if self.raise_exception_on_first and self.counter == 0: # pragma: no cover
            raise Exception('Test Exception') # pragma: no cover
        self.counter += 1 # pragma: no cover
        if self.counter > 2: # pragma: no cover
            raise StopAsyncIteration # pragma: no cover
        return f'Value {self.counter}' # pragma: no cover
 # pragma: no cover
def errback(failure_instance, *args, **kwargs): # pragma: no cover
    print(f'Errback executed with: {failure_instance}') # pragma: no cover
 # pragma: no cover
aiterable = MockAIterable(raise_exception_on_first=True) # pragma: no cover
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
