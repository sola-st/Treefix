from collections import defaultdict # pragma: no cover

self = type('Mock', (object,), {'inprogress': set()})() # pragma: no cover
request = 'sample_request' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
from l3.Runtime import _l_
self.inprogress.add(request)
_l_(5222)
