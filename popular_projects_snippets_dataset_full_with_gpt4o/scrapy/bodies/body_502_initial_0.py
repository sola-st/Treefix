data = 'some data' # pragma: no cover
self = type('Mock', (object,), {'out': ''})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testproc.py
from l3.Runtime import _l_
self.out += data
_l_(21431)
