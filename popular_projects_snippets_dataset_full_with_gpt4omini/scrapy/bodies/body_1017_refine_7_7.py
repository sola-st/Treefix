import asyncio # pragma: no cover
class MockSpider: # pragma: no cover
    pass # pragma: no cover
class MockResponse: # pragma: no cover
    pass # pragma: no cover
class MockSelf: # pragma: no cover
    async def _process_callback_output(self, response, spider, result): # pragma: no cover
        return 'processed output' # pragma: no cover

self = MockSelf() # pragma: no cover
response = MockResponse() # pragma: no cover
spider = MockSpider() # pragma: no cover
result = 'some result' # pragma: no cover

import asyncio # pragma: no cover
class MockSpider: # pragma: no cover
    pass # pragma: no cover
class MockResponse: # pragma: no cover
    pass # pragma: no cover
class MockSelf: # pragma: no cover
    async def _process_callback_output(self, response, spider, result): # pragma: no cover
        return {'processed': True, 'response': response, 'spider': spider, 'result': result} # pragma: no cover

self = MockSelf() # pragma: no cover
response = MockResponse() # pragma: no cover
spider = MockSpider() # pragma: no cover
result = {'data': 'example result'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(6241)
exit(aux)
