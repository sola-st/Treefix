import asyncio # pragma: no cover
import typing # pragma: no cover

self = type('Mock', (object,), {'_process_callback_output': lambda self, response, spider, result: asyncio.sleep(0)})() # pragma: no cover
response = type('Response', (object,), {'status': 200, 'text': 'OK'})() # pragma: no cover
spider = type('Spider', (object,), {'name': 'example_spider'})() # pragma: no cover
result = {'data': 'example_data'} # pragma: no cover

import asyncio # pragma: no cover

class Mock: # pragma: no cover
    async def _process_callback_output(self, response, spider, result): # pragma: no cover
        await asyncio.sleep(0.1) # pragma: no cover
        return 'processed_result' # pragma: no cover
 # pragma: no cover
self = Mock() # pragma: no cover
response = 'sample response' # pragma: no cover
spider = 'sample spider' # pragma: no cover
result = 'sample result' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(17093)
exit(aux)
