from typing import AsyncIterable # pragma: no cover
from unittest.mock import Mock # pragma: no cover

async def mock_async_iterable() -> AsyncIterable[int]: # pragma: no cover
    raise Exception('Test Exception') # pragma: no cover
 # pragma: no cover
aiterable = mock_async_iterable() # pragma: no cover
errback = Mock() # pragma: no cover
failure = Mock() # pragma: no cover
failure.Failure = Mock(return_value='An error occurred') # pragma: no cover
a = () # pragma: no cover
kw = {} # pragma: no cover

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
