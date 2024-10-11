import sqlite3 # pragma: no cover

self = type('MockSelf', (object,), {})() # pragma: no cover
self.db = sqlite3.connect(':memory:') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
from l3.Runtime import _l_
self.db.close()
_l_(17723)
