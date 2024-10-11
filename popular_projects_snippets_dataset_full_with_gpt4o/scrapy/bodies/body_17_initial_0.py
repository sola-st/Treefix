self = type('Mock', (object,), {'_stats': None})() # pragma: no cover
stats = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/statscollectors.py
from l3.Runtime import _l_
self._stats = stats
_l_(16078)
