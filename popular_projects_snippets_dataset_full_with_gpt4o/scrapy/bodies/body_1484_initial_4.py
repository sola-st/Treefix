from typing import Any # pragma: no cover
import logging # pragma: no cover
class MockSpider: pass # pragma: no cover
class MockCrawler: pass # pragma: no cover
class MockStats: pass # pragma: no cover
class MockRequest: pass # pragma: no cover
class Request: pass  # Placeholder for actual import if using a specific request class # pragma: no cover

request = MockRequest() # pragma: no cover
request.url = 'http://example.com/very/long/url/that/exceeds/maxlength' # pragma: no cover
self = type('MockSelf', (object,), {'maxlength': 50})() # pragma: no cover
logger = logging.getLogger() # pragma: no cover
spider = MockSpider() # pragma: no cover
spider.crawler = MockCrawler() # pragma: no cover
spider.crawler.stats = MockStats() # pragma: no cover
spider.crawler.stats.inc_value = lambda *args, **kwargs: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/urllength.py
from l3.Runtime import _l_
if isinstance(request, Request) and len(request.url) > self.maxlength:
    _l_(21129)

    logger.info(
        "Ignoring link (url length > %(maxlength)d): %(url)s ",
        {'maxlength': self.maxlength, 'url': request.url},
        extra={'spider': spider}
    )
    _l_(21126)
    spider.crawler.stats.inc_value('urllength/request_ignored_count', spider=spider)
    _l_(21127)
    aux = False
    _l_(21128)
    exit(aux)
aux = True
_l_(21130)
exit(aux)
