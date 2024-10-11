from typing import List # pragma: no cover

slot = type('Mock', (object,), {'active': set([1, 2, 3])})() # pragma: no cover
request = 1 # pragma: no cover
response = 'Exiting...' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/__init__.py
from l3.Runtime import _l_
slot.active.remove(request)
_l_(20665)
aux = response
_l_(20666)
exit(aux)
