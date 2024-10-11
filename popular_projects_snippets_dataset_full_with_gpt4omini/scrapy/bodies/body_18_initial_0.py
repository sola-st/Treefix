from collections import defaultdict # pragma: no cover

self = type('Mock', (object,), {'_stats': defaultdict(int)})() # pragma: no cover
key = 'example_key' # pragma: no cover
start = 0 # pragma: no cover
count = 5 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/statscollectors.py
from l3.Runtime import _l_
d = self._stats
_l_(9768)
d[key] = d.setdefault(key, start) + count
_l_(9769)
