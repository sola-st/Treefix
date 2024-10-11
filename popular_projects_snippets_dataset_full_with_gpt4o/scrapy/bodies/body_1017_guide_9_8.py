import asyncio # pragma: no cover
import sys # pragma: no cover

class MockSpider: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class Mock: # pragma: no cover
    async def _process_callback_output(self, response, spider, result): # pragma: no cover
        return 0  # or any other integer to simulate different outcomes # pragma: no cover
 # pragma: no cover
response = 'example_response' # pragma: no cover
spider = MockSpider() # pragma: no cover
result = 'example_result' # pragma: no cover
self = Mock() # pragma: no cover
 # pragma: no cover
async def execute_snippet(): # pragma: no cover
    aux = await self._process_callback_output(response, spider, result) # pragma: no cover
 # pragma: no cover
asyncio.run(execute_snippet()) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(17093)
exit(aux)
