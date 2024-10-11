import asyncio # pragma: no cover

class MockSpider: pass# pragma: no cover
spider = MockSpider() # pragma: no cover
response = 'mock_response' # pragma: no cover
result = 'mock_result' # pragma: no cover
class Mock: pass# pragma: no cover
self = type('Mock', (object,), {'_process_callback_output': asyncio.coroutine(lambda self, response, spider, result: 'callback_complete')})() # pragma: no cover

import asyncio # pragma: no cover

class MockSpider: pass # pragma: no cover
spider = MockSpider() # pragma: no cover
response = 'mock_response' # pragma: no cover
result = 'mock_result' # pragma: no cover
class Mock:# pragma: no cover
    async def _process_callback_output(self, response, spider, result):# pragma: no cover
        return 'callback_complete'# pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(17093)
exit(aux)
