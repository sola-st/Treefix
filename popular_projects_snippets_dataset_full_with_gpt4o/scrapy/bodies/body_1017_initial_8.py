import asyncio # pragma: no cover

response = 'mock_response' # pragma: no cover
spider = type('MockSpider', (object,), {})() # pragma: no cover
result = 'mock_result' # pragma: no cover
self = type('MockSelf', (object,), { '_process_callback_output': asyncio.coroutine(lambda self, response, spider, result: 'mock_output') })() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(17093)
exit(aux)
