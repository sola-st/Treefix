self = type('Mock', (object,), {'encoding': None})() # pragma: no cover
encoding = 'utf-8' # pragma: no cover
seq = [1, 2, 3] # pragma: no cover

class BaseClass:# pragma: no cover
    def __init__(self, seq):# pragma: no cover
        self.seq = seq # pragma: no cover
class Mock(BaseClass):# pragma: no cover
    def __init__(self, encoding, seq):# pragma: no cover
        self.encoding = encoding# pragma: no cover
        super().__init__(seq) # pragma: no cover
self = Mock('utf-8', [1, 2, 3]) # pragma: no cover
encoding = 'utf-8' # pragma: no cover
seq = [1, 2, 3] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/headers.py
from l3.Runtime import _l_
self.encoding = encoding
_l_(17527)
super().__init__(seq)
_l_(17528)
