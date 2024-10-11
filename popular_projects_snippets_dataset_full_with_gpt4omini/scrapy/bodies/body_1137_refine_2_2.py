from typing import List # pragma: no cover

self = type('Mock', (object,), {'encoding': None})() # pragma: no cover
encoding = 'utf-8' # pragma: no cover
seq = ['a', 'b', 'c'] # pragma: no cover

from typing import Any # pragma: no cover

self = type('Mock', (object,), {'encoding': None})() # pragma: no cover
class Base: # This is to provide a proper context for super() # pragma: no cover
    def __init__(self, seq): # pragma: no cover
        self.seq = seq # pragma: no cover
self.__class__ = type('Derived', (Base,), {}) # pragma: no cover
encoding = 'utf-8' # pragma: no cover
seq = 'example_sequence' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/headers.py
from l3.Runtime import _l_
self.encoding = encoding
_l_(6772)
super().__init__(seq)
_l_(6773)
