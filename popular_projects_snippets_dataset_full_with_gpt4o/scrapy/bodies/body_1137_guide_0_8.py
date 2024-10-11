class MockSuper: # pragma: no cover
    def __init__(self, seq): # pragma: no cover
        print('MockSuper initialized with seq:', seq) # pragma: no cover
object = type('MockSuper', (MockSuper,), {}) # pragma: no cover

encoding = 'utf-8' # pragma: no cover
seq = [1, 2, 3] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/headers.py
from l3.Runtime import _l_
self.encoding = encoding
_l_(17527)
super().__init__(seq)
_l_(17528)
