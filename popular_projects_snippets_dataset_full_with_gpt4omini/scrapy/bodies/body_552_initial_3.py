from collections import UserDict # pragma: no cover

class Mock(UserDict):# pragma: no cover
    def normkey(self, key): return key.lower()# pragma: no cover
    def normvalue(self, value): return value.strip() # pragma: no cover
self = Mock() # pragma: no cover
key = 'MyKey' # pragma: no cover
value = ' MyValue ' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/datatypes.py
from l3.Runtime import _l_
dict.__setitem__(self, self.normkey(key), self.normvalue(value))
_l_(10055)
