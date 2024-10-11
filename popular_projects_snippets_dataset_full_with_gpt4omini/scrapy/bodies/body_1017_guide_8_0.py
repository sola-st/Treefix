import asyncio # pragma: no cover
from unittest.mock import AsyncMock # pragma: no cover

response = 'mocked response' # pragma: no cover
spider = 'mocked spider' # pragma: no cover
result = 'mocked result' # pragma: no cover
self = type('MockSelf', (object,), {'_process_callback_output': AsyncMock(return_value='mocked output')})() # pragma: no cover
aux = asyncio.run(self._process_callback_output(response, spider, result)) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(6241)
exit(aux)
