import asyncio # pragma: no cover

self = type('Mock', (object,), {'_process_callback_output': lambda self, response, spider, result: asyncio.sleep(0.1)})() # pragma: no cover
response = 'dummy response' # pragma: no cover
spider = 'mock spider' # pragma: no cover
result = 'dummy result' # pragma: no cover

import asyncio # pragma: no cover

class MockSpider: pass # pragma: no cover
self = type('Mock', (object,), {'_process_callback_output': lambda self, response, spider, result: asyncio.sleep(0.1)})() # pragma: no cover
response = 'response_data' # pragma: no cover
spider = MockSpider() # pragma: no cover
result = 'result_data' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(17093)
exit(aux)
