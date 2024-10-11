from collections import defaultdict # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.normkey = lambda key: key.lower() # pragma: no cover
self.normvalue = lambda value: value.strip() # pragma: no cover
key = 'SOME_KEY' # pragma: no cover
value = '  Some Value  ' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/datatypes.py
from l3.Runtime import _l_
dict.__setitem__(self, self.normkey(key), self.normvalue(value))
_l_(10055)
