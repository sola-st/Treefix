import asyncio # pragma: no cover
import typing # pragma: no cover

self = type('Mock', (object,), {'_process_callback_output': lambda self, response, spider, result: asyncio.sleep(0)})() # pragma: no cover
response = type('Response', (object,), {'status': 200, 'text': 'OK'})() # pragma: no cover
spider = type('Spider', (object,), {'name': 'example_spider'})() # pragma: no cover
result = {'data': 'example_data'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(17093)
exit(aux)
