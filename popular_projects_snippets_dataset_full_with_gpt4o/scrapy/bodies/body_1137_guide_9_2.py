class MockSuperClass: # pragma: no cover
    def __init__(self, seq): # pragma: no cover
        self.seq = seq # pragma: no cover
 # pragma: no cover
seq = [1, 2, 3] # pragma: no cover
encoding = 'utf-8' # pragma: no cover
self = type('Mock', (MockSuperClass,), { '__init__': lambda self, seq, encoding: MockSuperClass.__init__(self, seq) or setattr(self, 'encoding', encoding)})(seq, encoding) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/headers.py
from l3.Runtime import _l_
self.encoding = encoding
_l_(17527)
super().__init__(seq)
_l_(17528)
