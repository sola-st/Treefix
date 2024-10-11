from typing import AsyncIterable, Callable, Any # pragma: no cover
from unittest.mock import Mock # pragma: no cover

aiterable = Mock(spec=AsyncIterable) # pragma: no cover
errback = Mock(spec=Callable) # pragma: no cover
failure = Mock() # pragma: no cover
failure.Failure = Mock(spec=Exception) # pragma: no cover
a = () # pragma: no cover
kw = {} # pragma: no cover

import asyncio # pragma: no cover
from typing import Callable, Any, AsyncIterable # pragma: no cover

class MockFailure:# pragma: no cover
    @staticmethod# pragma: no cover
    def Failure():# pragma: no cover
        return 'Mocked Failure'# pragma: no cover
# pragma: no cover
class MockAsyncIterable:# pragma: no cover
    def __init__(self, values):# pragma: no cover
        self.values = values# pragma: no cover
        self.index = 0# pragma: no cover
    def __aiter__(self):# pragma: no cover
        return self# pragma: no cover
    async def __anext__(self):# pragma: no cover
        if self.index < len(self.values):# pragma: no cover
            result = self.values[self.index]# pragma: no cover
            self.index += 1# pragma: no cover
            return result# pragma: no cover
        raise StopAsyncIteration# pragma: no cover
# pragma: no cover
aiterable = MockAsyncIterable([1, 2, 3])# pragma: no cover
errback = lambda failure_instance: print('Error occurred:', failure_instance)# pragma: no cover
failure = MockFailure# pragma: no cover
# pragma: no cover
a = ["arg1", "arg2"]# pragma: no cover
kw = {"key1": "value1", "key2": "value2"}# pragma: no cover
# pragma: no cover
async def run():# pragma: no cover
    it = aiterable.__aiter__()# pragma: no cover

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
