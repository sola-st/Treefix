from typing import Sequence # pragma: no cover

self = type('Mock', (object,), {'encoding': ''})() # pragma: no cover
encoding = 'utf-8' # pragma: no cover
seq = 'Hello, World!' # pragma: no cover

from typing import List # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/headers.py
from l3.Runtime import _l_
self.encoding = encoding
_l_(6772)
super().__init__(seq)
_l_(6773)
