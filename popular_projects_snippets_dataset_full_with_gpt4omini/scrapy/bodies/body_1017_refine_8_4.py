from unittest.mock import MagicMock # pragma: no cover

class MockSpider: pass # pragma: no cover
self = type('Mock', (object,), {'_process_callback_output': MagicMock(return_value='processed_output')})() # pragma: no cover
response = {'status': 'success', 'data': 'response data'} # pragma: no cover
spider = MockSpider() # pragma: no cover
result = {'result_key': 'result_value'} # pragma: no cover

import asyncio # pragma: no cover
from unittest.mock import AsyncMock # pragma: no cover

class MockSpider: pass # pragma: no cover
self = type('MockSelf', (object,), {'_process_callback_output': AsyncMock(return_value='processed_output')})() # pragma: no cover
response = {'status': 'success', 'data': 'response data'} # pragma: no cover
spider = MockSpider() # pragma: no cover
result = {'result_key': 'result_value'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(6241)
exit(aux)
