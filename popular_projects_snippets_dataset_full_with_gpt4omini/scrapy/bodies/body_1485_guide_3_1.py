import sys # pragma: no cover

class MockedError(NotImplementedError): pass # pragma: no cover
def raise_uncovered_path(): # pragma: no cover
    pass
raise_uncovered_path() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(5318)
