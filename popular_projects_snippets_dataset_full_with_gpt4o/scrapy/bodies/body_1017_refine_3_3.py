import asyncio # pragma: no cover

result = {'key': 'value'} # pragma: no cover
response = {'status': 200, 'data': 'some data'} # pragma: no cover
spider = type('Spider', (object,), {'name': 'test_spider'})() # pragma: no cover
self = type('Mock', (object,), {'_process_callback_output': asyncio.coroutine(lambda response, spider, result: 'processed_result')})() # pragma: no cover

import asyncio # pragma: no cover

class MockSpider: pass # pragma: no cover
async def process_callback_output(response, spider, result):# pragma: no cover
    await asyncio.sleep(0.1)# pragma: no cover
    return 'processed_output' # pragma: no cover
self = type('Mock', (object,), {'_process_callback_output': process_callback_output})() # pragma: no cover
response = 'response_data' # pragma: no cover
spider = MockSpider() # pragma: no cover
result = 'result_data' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(17093)
exit(aux)
