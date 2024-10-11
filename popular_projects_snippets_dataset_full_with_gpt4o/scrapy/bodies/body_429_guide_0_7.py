import asyncio # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover
from scrapy.utils.defer import failure # pragma: no cover

async def async_gen(): # pragma: no cover
    yield 1 # pragma: no cover
    raise Exception('Test exception') # pragma: no cover
aiterable = async_gen() # pragma: no cover
def errback(fail, *args, **kwargs): # pragma: no cover
    print('Error caught:', fail) # pragma: no cover
a = () # pragma: no cover
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
