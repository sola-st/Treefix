class Base: pass # pragma: no cover

class Mock(Base): # pragma: no cover
    def __init__(self, seq, encoding): # pragma: no cover
        self.encoding = encoding # pragma: no cover
self = Mock('example_sequence', 'utf-8') # pragma: no cover
encoding = 'utf-8' # pragma: no cover
seq = 'example_sequence' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/headers.py
from l3.Runtime import _l_
self.encoding = encoding
_l_(6772)
super().__init__(seq)
_l_(6773)
