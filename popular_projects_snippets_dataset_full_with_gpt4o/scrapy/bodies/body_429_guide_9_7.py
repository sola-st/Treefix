import asyncio # pragma: no cover
from twisted.python.failure import Failure # pragma: no cover

class MockAIterable: # pragma: no cover
    def __init__(self, items): # pragma: no cover
        self.items = items # pragma: no cover
        self.index = 0 # pragma: no cover
    def __aiter__(self): # pragma: no cover
        return self # pragma: no cover
    async def __anext__(self): # pragma: no cover
        if self.index >= len(self.items): # pragma: no cover
            raise StopAsyncIteration # pragma: no cover
        value = self.items[self.index] # pragma: no cover
        self.index += 1 # pragma: no cover
        if value == 'error': # pragma: no cover
            raise Exception('Test Exception') # pragma: no cover
        return value # pragma: no cover
 # pragma: no cover
def errback(failure_instance, *args, **kwargs): # pragma: no cover
    print(f'Error callback executed: {failure_instance}') # pragma: no cover
 # pragma: no cover
aiterable = MockAIterable([1, 'error', 3]) # pragma: no cover
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
