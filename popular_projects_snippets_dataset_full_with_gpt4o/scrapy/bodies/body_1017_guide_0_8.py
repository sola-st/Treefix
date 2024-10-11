import asyncio # pragma: no cover

class MockSpider: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class Mock: # pragma: no cover
    async def _process_callback_output(self, response, spider, result): # pragma: no cover
        return 0  # Replace with appropriate logic # pragma: no cover
 # pragma: no cover
self = Mock() # pragma: no cover
response = None  # Replace with actual response object if needed # pragma: no cover
spider = MockSpider() # pragma: no cover
result = None  # Replace with actual result object if needed # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(17093)
exit(aux)
