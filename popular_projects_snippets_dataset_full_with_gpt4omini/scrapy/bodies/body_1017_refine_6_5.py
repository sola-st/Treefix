import asyncio # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = Mock() # pragma: no cover
response = Mock() # pragma: no cover
spider = Mock() # pragma: no cover
result = Mock() # pragma: no cover
self._process_callback_output = Mock(return_value=asyncio.Future()) # pragma: no cover

import asyncio # pragma: no cover
from unittest.mock import AsyncMock # pragma: no cover

class MockSelf: # pragma: no cover
    async def _process_callback_output(self, response, spider, result): # pragma: no cover
        return {'processed': True, 'response': response, 'spider': spider, 'result': result} # pragma: no cover
self = MockSelf() # pragma: no cover
response = {'status': 200, 'content': 'Success'} # pragma: no cover
spider = {'name': 'example_spider'} # pragma: no cover
result = {'data': 'mock result'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(6241)
exit(aux)
