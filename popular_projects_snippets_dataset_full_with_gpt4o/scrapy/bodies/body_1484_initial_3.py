import logging # pragma: no cover
from collections import namedtuple # pragma: no cover
class MockSpider: pass # pragma: no cover
class MockCrawler: pass # pragma: no cover

Request = namedtuple('Request', ['url']) # pragma: no cover
request = Request(url='http://example.com') # pragma: no cover
self = type('MockSelf', (object,), {'maxlength': 20}) # pragma: no cover
logger = logging.getLogger('example_logger') # pragma: no cover
logging.basicConfig(level=logging.INFO) # pragma: no cover
spider = MockSpider() # pragma: no cover
spider.crawler = MockCrawler() # pragma: no cover

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
