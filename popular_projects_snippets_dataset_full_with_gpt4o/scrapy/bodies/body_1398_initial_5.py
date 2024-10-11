class MockClass:# pragma: no cover
    def __init__(self, instance):# pragma: no cover
        pass # pragma: no cover
self = MockClass(MockClass) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/item.py
from l3.Runtime import _l_
aux = self.__class__(self)
_l_(16363)
exit(aux)
