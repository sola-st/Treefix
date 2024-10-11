import logging # pragma: no cover
from scrapy.http import Request # pragma: no cover
from scrapy.crawler import Crawler # pragma: no cover

request = Request('http://example.com/very-long-url-exceeding-limit') # pragma: no cover
class MockSelf: maxlength = 50 # pragma: no cover
self = MockSelf() # pragma: no cover
logger = logging.getLogger('mock_logger') # pragma: no cover
class MockCrawler:  # Mocking Crawler # pragma: no cover
    def __init__(self): # pragma: no cover
        self.stats = type('MockStats', (object,), {'inc_value': lambda *args, **kwargs: None})() # pragma: no cover
spider = type('MockSpider', (object,), {'crawler': MockCrawler()})() # pragma: no cover

import logging # pragma: no cover
from scrapy.http import Request # pragma: no cover
from scrapy.crawler import Crawler # pragma: no cover

request = Request('http://example.com/very-long-url-exceeding-limit') # pragma: no cover
class MockSelf: maxlength = 50 # pragma: no cover
self = MockSelf() # pragma: no cover
logger = logging.getLogger('mock_logger') # pragma: no cover
logging.basicConfig(level=logging.INFO) # pragma: no cover
class MockStats:  # Mocking Stats # pragma: no cover
    def inc_value(self, name, spider=None): pass # pragma: no cover
class MockCrawler:  # Mocking Crawler # pragma: no cover
    def __init__(self): # pragma: no cover
        self.stats = MockStats() # pragma: no cover
spider = type('MockSpider', (object,), {'crawler': MockCrawler()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/urllength.py
from l3.Runtime import _l_
if isinstance(request, Request) and len(request.url) > self.maxlength:
    _l_(9979)

    logger.info(
        "Ignoring link (url length > %(maxlength)d): %(url)s ",
        {'maxlength': self.maxlength, 'url': request.url},
        extra={'spider': spider}
    )
    _l_(9976)
    spider.crawler.stats.inc_value('urllength/request_ignored_count', spider=spider)
    _l_(9977)
    aux = False
    _l_(9978)
    exit(aux)
aux = True
_l_(9980)
exit(aux)
