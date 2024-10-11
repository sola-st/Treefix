import asyncio # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = type('Mock', (object,), {'_process_callback_output': Mock(return_value=asyncio.Future() )})() # pragma: no cover
response = {'status': 200, 'data': 'example response'} # pragma: no cover
spider = {'name': 'example_spider', 'settings': {}} # pragma: no cover
result = {'key': 'value'} # pragma: no cover

import asyncio # pragma: no cover
from unittest.mock import AsyncMock # pragma: no cover

class MockSpider: pass # pragma: no cover
self = type('Mock', (object,), {'_process_callback_output': AsyncMock()})() # pragma: no cover
response = {'status': 200, 'data': 'example response'} # pragma: no cover
spider = MockSpider() # pragma: no cover
result = {'key': 'value'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(6241)
exit(aux)
