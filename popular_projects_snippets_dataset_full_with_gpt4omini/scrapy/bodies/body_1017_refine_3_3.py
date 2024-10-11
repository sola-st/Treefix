import asyncio # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = type('MockSelf', (object,), {'_process_callback_output': Mock(return_value=asyncio.Future() )})() # pragma: no cover
response = {'status': 200, 'data': 'Success'} # pragma: no cover
spider = {'name': 'test_spider'} # pragma: no cover
result = {'key': 'value'} # pragma: no cover

import asyncio # pragma: no cover
from unittest.mock import Mock # pragma: no cover

async def mock_process_callback_output(response, spider, result): return result # pragma: no cover
self = type('Mock', (object,), {'_process_callback_output': mock_process_callback_output})() # pragma: no cover
response = {'status': 200, 'data': 'mock data'} # pragma: no cover
spider = {'name': 'example_spider'} # pragma: no cover
result = {'key': 'value'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(6241)
exit(aux)
