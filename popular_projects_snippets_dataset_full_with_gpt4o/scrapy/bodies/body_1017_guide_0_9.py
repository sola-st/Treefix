import asyncio # pragma: no cover

class Spider: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class MockObject: # pragma: no cover
    async def _process_callback_output(self, response, spider, result): # pragma: no cover
        return 0  # Assuming a simple return for demonstration # pragma: no cover
 # pragma: no cover
self = MockObject() # pragma: no cover
response = None # pragma: no cover
spider = Spider() # pragma: no cover
result = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(17093)
exit(aux)
