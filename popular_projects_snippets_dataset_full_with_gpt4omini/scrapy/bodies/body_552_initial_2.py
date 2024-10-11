from typing import Dict # pragma: no cover

self = type('Mock', (object,), {'normkey': lambda self, key: str(key).upper(), 'normvalue': lambda self, value: str(value)})() # pragma: no cover
key = 'exampleKey' # pragma: no cover
value = 'exampleValue' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/datatypes.py
from l3.Runtime import _l_
dict.__setitem__(self, self.normkey(key), self.normvalue(value))
_l_(10055)
