from itertools import chain # pragma: no cover

self = type('MockSelf', (object,), {})() # pragma: no cover
chain = chain # pragma: no cover
args = [[1, 2], [3, 4]] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/python.py
from l3.Runtime import _l_
self.data = chain.from_iterable(args)
_l_(19821)
