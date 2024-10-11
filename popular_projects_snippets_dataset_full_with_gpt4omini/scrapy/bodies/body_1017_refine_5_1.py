from typing import Any, Awaitable # pragma: no cover
from unittest.mock import AsyncMock # pragma: no cover

self = type('Mock', (object,), {'_process_callback_output': AsyncMock()})() # pragma: no cover
response = {'status': 200, 'body': 'OK'} # pragma: no cover
spider = 'my_spider' # pragma: no cover
result = {'data': 'sample_result'} # pragma: no cover

import asyncio # pragma: no cover
from unittest.mock import AsyncMock # pragma: no cover

class MockSelf:# pragma: no cover
    async def _process_callback_output(self, response, spider, result):# pragma: no cover
        return {'processed': True, 'response': response, 'spider': spider, 'result': result}# pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover
response = {'status': 200, 'data': 'response data'} # pragma: no cover
spider = 'example_spider' # pragma: no cover
result = {'key': 'value'} # pragma: no cover
asyncio.run(self._process_callback_output(response, spider, result)) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(6241)
exit(aux)
