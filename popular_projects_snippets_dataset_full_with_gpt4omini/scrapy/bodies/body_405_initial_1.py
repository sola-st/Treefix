from collections import UserDict # pragma: no cover

self = type('Mock', (UserDict,), {'attributes': ['value1', 'value2', 'value3']})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
from l3.Runtime import _l_
aux = iter(self.attributes)
_l_(9604)
exit(aux)
