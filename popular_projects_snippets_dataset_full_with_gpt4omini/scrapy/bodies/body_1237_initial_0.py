from unittest.mock import MagicMock # pragma: no cover

self = type('Mock', (object,), {'indent': 1, 'xg': MagicMock()})() # pragma: no cover
new_item = False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exporters.py
from l3.Runtime import _l_
if self.indent is not None and (self.indent > 0 or new_item):
    _l_(9872)

    self.xg.characters('\n')
    _l_(9871)
