from unittest.mock import MagicMock # pragma: no cover

errback = MagicMock() # pragma: no cover
failure = type('Mock', (object,), {'Failure': MagicMock()}) # pragma: no cover
a = [] # pragma: no cover
kw = {} # pragma: no cover

import asyncio # pragma: no cover
from unittest.mock import AsyncMock, Mock # pragma: no cover

class MockFailure:# pragma: no cover
    @staticmethod# pragma: no cover
    def Failure():# pragma: no cover
        return 'Failure instance' # pragma: no cover
aiterable = AsyncMock() # pragma: no cover
aiterable.__aiter__.return_value = aiterable # pragma: no cover
aiterable.__anext__.side_effect = [1, 2, 3, StopAsyncIteration] # pragma: no cover
failure = MockFailure() # pragma: no cover
a = ["arg1", "arg2"] # pragma: no cover
kw = {"key1": "value1", "key2": "value2"} # pragma: no cover
async def main():# pragma: no cover
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
