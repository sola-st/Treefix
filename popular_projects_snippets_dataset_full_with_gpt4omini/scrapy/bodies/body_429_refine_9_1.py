from typing import AsyncIterable, Callable, Any # pragma: no cover
from unittest.mock import Mock # pragma: no cover

aiterable = Mock(spec=AsyncIterable) # pragma: no cover
async def mock_aiter(self): return self # pragma: no cover
def errback(failure, *args, **kwargs): pass # pragma: no cover
failure = Mock() # pragma: no cover
failure.Failure = Mock() # pragma: no cover
a = [] # pragma: no cover
kw = {} # pragma: no cover

import asyncio # pragma: no cover
from unittest.mock import AsyncMock # pragma: no cover

class MockAsyncIterable:  # Mock class to simulate async iteration # pragma: no cover
    def __aiter__(self): # pragma: no cover
        self.index = 0 # pragma: no cover
        self.data = [1, 2, 3] # pragma: no cover
        return self # pragma: no cover
    async def __anext__(self): # pragma: no cover
        if self.index < len(self.data): # pragma: no cover
            result = self.data[self.index] # pragma: no cover
            self.index += 1 # pragma: no cover
            return result # pragma: no cover
        raise StopAsyncIteration # pragma: no cover
aiterable = MockAsyncIterable() # pragma: no cover
async def errback(*args, **kwargs): print('Error:', args, kwargs) # pragma: no cover
failure = type('MockFailure', (object,), {'Failure': lambda: 'MockFailure raised'}) # pragma: no cover
a = () # pragma: no cover
kw = {} # pragma: no cover
async def main(): pass # pragma: no cover
asyncio.run(main()) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/defer.py
from l3.Runtime import _l_
"""Wraps an async iterable calling an errback if an error is caught while
    iterating it. Similar to scrapy.utils.defer.iter_errback()
    """
it = aiterable.__aiter__()
_l_(9015)
while True:
    _l_(9022)

    try:
        _l_(9021)

        aux = await it.__anext__()
        _l_(9016)
        exit(aux)
    except StopAsyncIteration:
        _l_(9018)

        break
        _l_(9017)
    except Exception:
        _l_(9020)

        errback(failure.Failure(), *a, **kw)
        _l_(9019)
