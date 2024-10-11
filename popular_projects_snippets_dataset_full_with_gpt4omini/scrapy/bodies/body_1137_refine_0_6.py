from typing import Any, List # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
encoding = 'utf-8' # pragma: no cover
seq = 'Hello, World!' # pragma: no cover

from typing import Any, List # pragma: no cover

class MockBase: pass # pragma: no cover
self = type('Mock', (MockBase,), {'encoding': None})() # pragma: no cover
encoding = 'utf-8' # pragma: no cover
seq = 'Hello, World!' # pragma: no cover
MockBase.__init__ = lambda self, seq: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/headers.py
from l3.Runtime import _l_
self.encoding = encoding
_l_(6772)
super().__init__(seq)
_l_(6773)
