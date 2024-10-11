import asyncio # pragma: no cover

self = type('Mock', (object,), {'_process_callback_output': lambda self, response, spider, result: response + spider + result})() # pragma: no cover
response = 1 # pragma: no cover
spider = 2 # pragma: no cover
result = 3 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(17093)
exit(aux)
