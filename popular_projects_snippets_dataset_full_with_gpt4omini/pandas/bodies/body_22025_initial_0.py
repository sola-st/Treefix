from itertools import groupby # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
groupby_object = groupby([], key=lambda x: x) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/groupby/indexing.py
from l3.Runtime import _l_
self.groupby_object = groupby_object
_l_(10389)
