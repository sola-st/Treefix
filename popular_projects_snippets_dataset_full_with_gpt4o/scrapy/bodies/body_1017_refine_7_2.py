import asyncio # pragma: no cover

self = type('Mock', (object,), {'_process_callback_output': lambda self, response, spider, result: response + spider + result})() # pragma: no cover
response = 1 # pragma: no cover
spider = 2 # pragma: no cover
result = 3 # pragma: no cover

import asyncio # pragma: no cover

class Spider: pass# pragma: no cover
spider = Spider() # pragma: no cover
response = 'response_value' # pragma: no cover
result = 'result_value' # pragma: no cover
class Mock:# pragma: no cover
    async def _process_callback_output(self, response, spider, result):# pragma: no cover
        return 'processed_output'# pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(17093)
exit(aux)
