from typing import Any # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
encoding = 'utf-8' # pragma: no cover
seq = [b'example', b'text'] # pragma: no cover

from typing import Any # pragma: no cover

class BaseClass: pass # pragma: no cover
self = type('Mock', (BaseClass,), {'encoding': None})() # pragma: no cover
encoding = 'utf-8' # pragma: no cover
seq = 'example_sequence' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/headers.py
from l3.Runtime import _l_
self.encoding = encoding
_l_(6772)
super().__init__(seq)
_l_(6773)
