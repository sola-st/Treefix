from typing import Any, List # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
encoding = 'utf-8' # pragma: no cover
seq = [1, 2, 3] # pragma: no cover

from typing import Any, List # pragma: no cover

class Base: pass # pragma: no cover
self = type('Mock', (Base,), {'encoding': None})() # pragma: no cover
encoding = 'utf-8' # pragma: no cover
seq = 'sample_sequence' # pragma: no cover
Base.__init__ = lambda self, seq: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/headers.py
from l3.Runtime import _l_
self.encoding = encoding
_l_(6772)
super().__init__(seq)
_l_(6773)
