from types import FunctionType # pragma: no cover

class MockCrawler: pass # pragma: no cover
cls = type('MockClass', (object,), {'__init__': lambda self, crawler: None}) # pragma: no cover
crawler = MockCrawler() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/request.py
from l3.Runtime import _l_
aux = cls(crawler)
_l_(8891)
exit(aux)
