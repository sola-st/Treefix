import sys # pragma: no cover

def raise_not_implemented(): # pragma: no cover
    raise NotImplementedError('This feature is not implemented') # pragma: no cover
sys.modules[__name__].raise_not_implemented = raise_not_implemented # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(5318)
