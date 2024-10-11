from typing import Any, Dict, Optional # pragma: no cover

import asyncio # pragma: no cover
from unittest.mock import Mock # pragma: no cover

class MockSpider: pass # pragma: no cover
async def mock_process_callback_output(response, spider, result): return {'processed': True, 'response': response, 'spider': spider, 'result': result} # pragma: no cover
self = type('MockSelf', (object,), {'_process_callback_output': mock_process_callback_output})() # pragma: no cover
response = {'status': 200, 'data': 'mocked response'} # pragma: no cover
spider = MockSpider() # pragma: no cover
result = {'outcome': 'success'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(6241)
exit(aux)
