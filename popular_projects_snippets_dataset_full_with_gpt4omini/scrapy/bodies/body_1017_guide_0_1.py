import asyncio # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

self = type('Mock', (object,), {'_process_callback_output': MagicMock(return_value='Processed Result')})() # pragma: no cover
response = 'Mock Response' # pragma: no cover
spider = 'Mock Spider' # pragma: no cover
result = 'Mock Result' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(6241)
exit(aux)
