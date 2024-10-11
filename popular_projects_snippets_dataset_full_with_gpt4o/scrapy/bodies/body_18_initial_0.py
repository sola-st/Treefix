self = type('Mock', (object,), {'_stats': {}})() # pragma: no cover
key = 'example_key' # pragma: no cover
start = 10 # pragma: no cover
count = 5 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/statscollectors.py
from l3.Runtime import _l_
d = self._stats
_l_(20992)
d[key] = d.setdefault(key, start) + count
_l_(20993)
