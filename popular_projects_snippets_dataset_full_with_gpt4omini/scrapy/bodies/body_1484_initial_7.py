class MockRequest:# pragma: no cover
    def __init__(self, url):# pragma: no cover
        self.url = url# pragma: no cover
# pragma: no cover
request = MockRequest(url='http://example.com/some/very/long/url/that/exceeds/the/maxlength') # pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.maxlength = 50# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
class MockCrawler:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.stats = self# pragma: no cover
    def inc_value(self, key, spider):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
class MockSpider:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.crawler = MockCrawler()# pragma: no cover
# pragma: no cover
spider = MockSpider() # pragma: no cover

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
