from typing import Any, Dict # pragma: no cover
import asyncio # pragma: no cover

class MockSpider: pass # pragma: no cover
self = type('Mock', (object,), {'_process_callback_output': lambda self, resp, spd, res: asyncio.sleep(0)})() # pragma: no cover
response = {'status': 200, 'body': 'mock response'} # pragma: no cover
spider = MockSpider() # pragma: no cover
result = {'data': 'mock result'} # pragma: no cover

from typing import Any, Dict # pragma: no cover
import asyncio # pragma: no cover

class MockSpider: pass # pragma: no cover
async def mock_process_callback_output(response: Any, spider: MockSpider, result: Any): return result # pragma: no cover
self = type('Mock', (object,), {'_process_callback_output': mock_process_callback_output})() # pragma: no cover
response = {'status': 200, 'body': 'mock response'} # pragma: no cover
spider = MockSpider() # pragma: no cover
result = {'data': 'mock result'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(6241)
exit(aux)
