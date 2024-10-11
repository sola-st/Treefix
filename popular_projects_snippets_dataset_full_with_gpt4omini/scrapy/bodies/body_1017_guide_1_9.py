import asyncio # pragma: no cover
from unittest.mock import AsyncMock # pragma: no cover

class MockSpider: pass # pragma: no cover
class MockResult: pass # pragma: no cover
response = AsyncMock() # pragma: no cover
spider = MockSpider() # pragma: no cover
result = MockResult() # pragma: no cover
self = type('MockSelf', (object,), {'_process_callback_output': AsyncMock(return_value='processed_output')})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(6241)
exit(aux)
