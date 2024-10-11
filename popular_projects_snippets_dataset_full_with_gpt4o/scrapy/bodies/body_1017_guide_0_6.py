import asyncio # pragma: no cover

class MockSpider: # pragma: no cover
    # Placeholder for the Spider class # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class Mock: # pragma: no cover
    def __init__(self): # pragma: no cover
        self._process_callback_output = asyncio.coroutine(lambda response, spider, result: True) # pragma: no cover
 # pragma: no cover
response = None # pragma: no cover
spider = MockSpider() # pragma: no cover
result = None # pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(17093)
exit(aux)
