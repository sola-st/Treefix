import asyncio # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = Mock() # pragma: no cover
response = Mock() # pragma: no cover
spider = Mock() # pragma: no cover
result = Mock() # pragma: no cover
self._process_callback_output = Mock(return_value=asyncio.Future()) # pragma: no cover

from typing import Any, Dict # pragma: no cover
import asyncio # pragma: no cover

class MockSpider: pass # pragma: no cover
class MockSelf: # pragma: no cover
    async def _process_callback_output(self, response: Any, spider: MockSpider, result: Any) -> Dict[str, Any]: # pragma: no cover
        return {'output': result} # pragma: no cover
self = MockSelf() # pragma: no cover
response = {'status': 200, 'body': 'success'} # pragma: no cover
spider = MockSpider() # pragma: no cover
result = {'data': 'example result'} # pragma: no cover
asyncio.run(self._process_callback_output(response, spider, result)) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(6241)
exit(aux)
