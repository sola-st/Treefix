from typing import List # pragma: no cover

class MockActive:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.items = []# pragma: no cover
    def remove(self, item):# pragma: no cover
        self.items.remove(item) # pragma: no cover
slot = type('MockSlot', (object,), {'active': MockActive()})() # pragma: no cover
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
