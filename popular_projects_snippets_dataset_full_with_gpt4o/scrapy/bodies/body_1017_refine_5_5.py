import asyncio # pragma: no cover

response = 'mock_response' # pragma: no cover
spider = 'mock_spider' # pragma: no cover
result = 'mock_result' # pragma: no cover
self = type('MockSelf', (object,), {'_process_callback_output': lambda self, response, spider, result: 'processed_output'})() # pragma: no cover

import asyncio # pragma: no cover

response = 'mock_response' # pragma: no cover
spider = 'mock_spider' # pragma: no cover
result = 'mock_result' # pragma: no cover
self = type('MockSelf', (object,), {'_process_callback_output': lambda self, response, spider, result: asyncio.sleep(0.1)})() # pragma: no cover
async def main(): # pragma: no cover
    await self._process_callback_output(response, spider, result) # pragma: no cover
asyncio.run(main()) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(17093)
exit(aux)
