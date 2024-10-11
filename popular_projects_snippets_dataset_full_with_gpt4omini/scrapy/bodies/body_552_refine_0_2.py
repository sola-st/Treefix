from collections import UserDict # pragma: no cover

class Mock(UserDict): # pragma: no cover
    def normkey(self, key): return key.strip() if isinstance(key, str) else key # pragma: no cover
    def normvalue(self, value): return value if value is not None else 'default_value' # pragma: no cover
self = Mock() # pragma: no cover
key = ' example_key ' # pragma: no cover
value = None # pragma: no cover

class Mock(dict): # pragma: no cover
    def normkey(self, key): return key.strip() if isinstance(key, str) else key # pragma: no cover
    def normvalue(self, value): return value if value is not None else 'default_value' # pragma: no cover
self = Mock() # pragma: no cover
key = ' example_key ' # pragma: no cover
value = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/datatypes.py
from l3.Runtime import _l_
dict.__setitem__(self, self.normkey(key), self.normvalue(value))
_l_(10055)
