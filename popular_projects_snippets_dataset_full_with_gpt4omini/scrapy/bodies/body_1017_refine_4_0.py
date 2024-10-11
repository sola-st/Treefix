from typing import Any, Dict, Optional # pragma: no cover

import asyncio # pragma: no cover
from unittest.mock import AsyncMock # pragma: no cover

class MockSpider: pass # pragma: no cover
self = type('MockSelf', (object,), {'_process_callback_output': AsyncMock()})() # pragma: no cover
response = {'status': 200, 'data': 'example data'} # pragma: no cover
spider = MockSpider() # pragma: no cover
result = {'key': 'value'} # pragma: no cover
async def main(): # pragma: no cover
    return await self._process_callback_output(response, spider, result) # pragma: no cover
asyncio.run(main()) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(6241)
exit(aux)
