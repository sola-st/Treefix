import asyncio # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = Mock() # pragma: no cover
response = Mock() # pragma: no cover
spider = Mock() # pragma: no cover
result = Mock() # pragma: no cover
self._process_callback_output = Mock(return_value=asyncio.Future()) # pragma: no cover

import asyncio # pragma: no cover
from unittest.mock import AsyncMock # pragma: no cover

class MockSpider: pass # pragma: no cover
self = type('MockSelf', (object,), {'_process_callback_output': AsyncMock()})() # pragma: no cover
response = {'status': 200, 'body': 'Mock response data'} # pragma: no cover
spider = MockSpider() # pragma: no cover
result = {'key': 'value'} # pragma: no cover
self._process_callback_output.return_value = asyncio.Future() # pragma: no cover
self._process_callback_output.return_value.set_result(result) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(6241)
exit(aux)
