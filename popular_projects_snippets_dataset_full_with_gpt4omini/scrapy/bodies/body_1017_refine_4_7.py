from typing import Any, Dict, Optional # pragma: no cover

import asyncio # pragma: no cover
from unittest.mock import Mock # pragma: no cover

class MockSpider: pass # pragma: no cover
class MockSelf: # pragma: no cover
    async def _process_callback_output(self, response, spider, result): # pragma: no cover
        return {'status': 'processed', 'response': response, 'spider': spider, 'result': result} # pragma: no cover
self = MockSelf() # pragma: no cover
response = {'status': 200, 'body': b'mock response'} # pragma: no cover
spider = MockSpider() # pragma: no cover
result = {'key': 'value'} # pragma: no cover
async def main(): # pragma: no cover
    return await self._process_callback_output(response, spider, result) # pragma: no cover
loop = asyncio.get_event_loop() # pragma: no cover
output = loop.run_until_complete(main()) # pragma: no cover
print(output) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(6241)
exit(aux)
