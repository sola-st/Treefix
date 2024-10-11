self = type('Mock', (object,), {'active_size': 10, 'max_active_size': 5})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/scraper.py
from l3.Runtime import _l_
aux = self.active_size > self.max_active_size
_l_(17979)
exit(aux)
