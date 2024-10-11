class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.active_size = 10 # pragma: no cover
self.max_active_size = 5 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/scraper.py
from l3.Runtime import _l_
aux = self.active_size > self.max_active_size
_l_(7553)
exit(aux)
