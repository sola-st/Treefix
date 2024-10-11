import asyncio # pragma: no cover
from unittest.mock import AsyncMock # pragma: no cover

response = 'mock response' # pragma: no cover
spider = 'mock spider' # pragma: no cover
result = 'mock result' # pragma: no cover
self = type('MockSelf', (object,), {'_process_callback_output': AsyncMock(return_value='mocked_output')})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(6241)
exit(aux)
