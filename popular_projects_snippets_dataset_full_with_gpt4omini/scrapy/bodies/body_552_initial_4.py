from collections import UserDict # pragma: no cover

self = type('Mock', (UserDict,), {'normkey': lambda self, x: x, 'normvalue': lambda self, x: x})() # pragma: no cover
key = 'example_key' # pragma: no cover
value = 'example_value' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/datatypes.py
from l3.Runtime import _l_
dict.__setitem__(self, self.normkey(key), self.normvalue(value))
_l_(10055)
