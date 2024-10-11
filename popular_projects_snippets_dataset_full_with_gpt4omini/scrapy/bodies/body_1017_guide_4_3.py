import asyncio # pragma: no cover
from unittest.mock import AsyncMock, MagicMock # pragma: no cover

response = MagicMock() # pragma: no cover
spider = MagicMock() # pragma: no cover
result = MagicMock() # pragma: no cover
self = type('Mock', (object,), {'_process_callback_output': AsyncMock(return_value='mocked_output')})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(6241)
exit(aux)
