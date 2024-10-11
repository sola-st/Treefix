import asyncio # pragma: no cover
from types import SimpleNamespace # pragma: no cover

response = SimpleNamespace() # pragma: no cover
spider = SimpleNamespace() # pragma: no cover
result = SimpleNamespace() # pragma: no cover
self = SimpleNamespace() # pragma: no cover
self._process_callback_output = lambda r, s, res: asyncio.sleep(0) or 'processed' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
from l3.Runtime import _l_
aux = await self._process_callback_output(response, spider, result)
_l_(6241)
exit(aux)
