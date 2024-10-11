import asyncio # pragma: no cover

result = {'key': 'value'} # pragma: no cover
response = {'status': 200, 'data': 'some data'} # pragma: no cover
spider = type('Spider', (object,), {'name': 'test_spider'})() # pragma: no cover
self = type('Mock', (object,), {'_process_callback_output': asyncio.coroutine(lambda response, spider, result: 'processed_result')})() # pragma: no cover

import asyncio # pragma: no cover

result = 'result_data' # pragma: no cover
response = 'response_data' # pragma: no cover
spider = type('Spider', (object,), {'name': 'dummy_spider'})() # pragma: no cover
self = type('Mock', (object,), {'_process_callback_output': lambda self, response, spider, result: asyncio.sleep(1)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(17093)
exit(aux)
