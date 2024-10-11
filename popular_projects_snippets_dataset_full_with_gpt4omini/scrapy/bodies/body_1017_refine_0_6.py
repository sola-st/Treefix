from typing import Any # pragma: no cover
class MockSpider: # pragma: no cover
    pass # pragma: no cover
async def mock_process_callback_output(response: Any, spider: MockSpider, result: Any): # pragma: no cover
    return result # pragma: no cover

self = type('Mock', (object,), {'_process_callback_output': mock_process_callback_output})() # pragma: no cover
response = {'status': 200, 'data': 'some data'} # pragma: no cover
spider = MockSpider() # pragma: no cover
result = {'success': True, 'message': 'Operation completed successfully.'} # pragma: no cover

from typing import Any, Coroutine # pragma: no cover
class MockSpider: # pragma: no cover
    pass # pragma: no cover
async def mock_process_callback_output(response: Any, spider: MockSpider, result: Any) -> Any: # pragma: no cover
    return result # pragma: no cover
import asyncio # pragma: no cover

self = type('Mock', (object,), {'_process_callback_output': mock_process_callback_output})() # pragma: no cover
response = {'status': 200, 'data': 'some data'} # pragma: no cover
spider = MockSpider() # pragma: no cover
result = {'success': True, 'message': 'Operation completed successfully.'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(6241)
exit(aux)
