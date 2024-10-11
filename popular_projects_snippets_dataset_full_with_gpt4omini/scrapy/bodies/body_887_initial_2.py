from scrapy.settings import Settings # pragma: no cover
from scrapy.crawler import Crawler # pragma: no cover

class MockClass:# pragma: no cover
    def __init__(self, settings, crawler):# pragma: no cover
        self.settings = settings# pragma: no cover
# pragma: no cover
cls = MockClass# pragma: no cover
# pragma: no cover
mock_settings = Settings()# pragma: no cover
# pragma: no cover
class MockCrawler:# pragma: no cover
    def __init__(self, settings):# pragma: no cover
        self.settings = settings# pragma: no cover
# pragma: no cover
crawler = MockCrawler(mock_settings) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
aux = cls(crawler.settings, crawler)
_l_(7716)
exit(aux)
