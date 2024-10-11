from typing import List, Any # pragma: no cover

slot = type('MockSlot', (object,), {'active': []})() # pragma: no cover
request = 'sample_request' # pragma: no cover
response = 'sample_response' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/__init__.py
from l3.Runtime import _l_
slot.active.remove(request)
_l_(9179)
aux = response
_l_(9180)
exit(aux)
