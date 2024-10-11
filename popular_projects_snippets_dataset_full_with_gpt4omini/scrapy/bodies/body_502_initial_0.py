class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.out = '' # pragma: no cover
data = 'example data' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testproc.py
from l3.Runtime import _l_
self.out += data
_l_(10037)
