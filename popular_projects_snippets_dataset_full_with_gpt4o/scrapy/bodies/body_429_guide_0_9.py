import asyncio # pragma: no cover
from twisted.python import failure # pragma: no cover

class MockAsyncIterable: # pragma: no cover
    def __init__(self, items): # pragma: no cover
        self._items = items # pragma: no cover
        self._index = 0 # pragma: no cover
 # pragma: no cover
    def __aiter__(self): # pragma: no cover
        return self # pragma: no cover
 # pragma: no cover
    async def __anext__(self): # pragma: no cover
        if self._index >= len(self._items): # pragma: no cover
            raise StopAsyncIteration # pragma: no cover
        item = self._items[self._index] # pragma: no cover
        self._index += 1 # pragma: no cover
        return item # pragma: no cover
 # pragma: no cover
async def mock_errback(*args, **kwargs): # pragma: no cover
    print(f'Error caught: {args}, {kwargs}') # pragma: no cover
 # pragma: no cover
mock_items = [1, 2, 3] # pragma: no cover
aiterable = MockAsyncIterable(mock_items) # pragma: no cover
errback = mock_errback # pragma: no cover
a, kw = [], {} # pragma: no cover

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
