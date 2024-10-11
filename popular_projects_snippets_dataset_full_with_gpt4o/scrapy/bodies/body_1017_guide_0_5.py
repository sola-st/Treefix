import asyncio # pragma: no cover

class SpiderMock: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class SelfMock: # pragma: no cover
    async def _process_callback_output(self, response, spider, result): # pragma: no cover
        return response + result # pragma: no cover
 # pragma: no cover
self = SelfMock() # pragma: no cover
response = 5 # pragma: no cover
spider = SpiderMock() # pragma: no cover
result = 10 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(17093)
exit(aux)
