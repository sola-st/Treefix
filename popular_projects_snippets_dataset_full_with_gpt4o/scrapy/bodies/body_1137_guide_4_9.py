class MockSuperClass: # pragma: no cover
    def __init__(self, seq): # pragma: no cover
        self.seq = seq # pragma: no cover
 # pragma: no cover
class MyClass(MockSuperClass): # pragma: no cover
    def __init__(self, seq, encoding): # pragma: no cover
        self.encoding = encoding # pragma: no cover
        super().__init__(seq) # pragma: no cover
 # pragma: no cover
seq = [1, 2, 3] # pragma: no cover
encoding = 'utf-8' # pragma: no cover
obj = MyClass(seq, encoding) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/headers.py
from l3.Runtime import _l_
self.encoding = encoding
_l_(17527)
super().__init__(seq)
_l_(17528)
