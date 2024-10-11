from crawler import Crawler # pragma: no cover

class MockSettings:# pragma: no cover
    pass # pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.settings = MockSettings() # pragma: no cover
crawler = Mock() # pragma: no cover
cls = Crawler # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
aux = cls(crawler.settings, crawler)
_l_(7716)
exit(aux)
