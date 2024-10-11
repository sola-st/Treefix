import asyncio # pragma: no cover
from unittest.mock import Mock # pragma: no cover

response = Mock() # pragma: no cover
spider = Mock() # pragma: no cover
result = Mock() # pragma: no cover
self = type('MockSelf', (object,), {'_process_callback_output': asyncio.Future()})() # pragma: no cover
self._process_callback_output.set_result('processed_output') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(6241)
exit(aux)
