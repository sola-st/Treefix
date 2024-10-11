import sys # pragma: no cover
import asyncio # pragma: no cover

class MockSpider: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    async def _process_callback_output(self, response, spider, result): # pragma: no cover
        return 0  # Return a concrete value to trigger sys.exit # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover
response = 'example_response' # pragma: no cover
spider = MockSpider() # pragma: no cover
result = 'example_result' # pragma: no cover
 # pragma: no cover
async def main(): # pragma: no cover
    # Execute the code snippet # pragma: no cover
    aux = await self._process_callback_output(response, spider, result) # pragma: no cover
 # pragma: no cover
asyncio.run(main()) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(17093)
exit(aux)
