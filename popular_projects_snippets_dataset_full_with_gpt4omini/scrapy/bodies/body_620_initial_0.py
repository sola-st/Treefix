from itertools import chain # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
args = [[1, 2, 3], [4, 5], [6]] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/python.py
from l3.Runtime import _l_
self.data = chain.from_iterable(args)
_l_(8852)
