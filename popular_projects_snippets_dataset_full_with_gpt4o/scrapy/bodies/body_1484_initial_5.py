from types import SimpleNamespace # pragma: no cover
from unittest.mock import Mock # pragma: no cover
import logging # pragma: no cover

request = SimpleNamespace(url='http://example.com/very/long/url') # pragma: no cover
Request = type('Request', (object,), {}) # pragma: no cover
self = SimpleNamespace(maxlength=50) # pragma: no cover
logger = Mock() # pragma: no cover
logger.info = Mock() # pragma: no cover
spider = SimpleNamespace() # pragma: no cover
spider.crawler = SimpleNamespace() # pragma: no cover
spider.crawler.stats = Mock() # pragma: no cover
spider.crawler.stats.inc_value = Mock() # pragma: no cover

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
