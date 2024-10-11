from scrapy.http import Request # pragma: no cover
import logging # pragma: no cover
from scrapy.crawler import Crawler # pragma: no cover

request = Request(url='http://example.com/very/long/url/that/exceeds/the/maxlength') # pragma: no cover
Request = type('Request', (object,), {}) # pragma: no cover
self = type('MockSelf', (object,), {'maxlength': 50})() # pragma: no cover
logger = logging.getLogger('test_logger') # pragma: no cover

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
