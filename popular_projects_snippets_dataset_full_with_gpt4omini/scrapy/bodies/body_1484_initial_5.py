from unittest.mock import MagicMock # pragma: no cover
import logging # pragma: no cover

request = MagicMock(url='http://example.com/some/uri/that/is/definitely/long') # pragma: no cover
Request = type('Request', (object,), {}) # pragma: no cover
self = type('Self', (object,), {'maxlength': 40})() # pragma: no cover
logger = logging.getLogger('test_logger') # pragma: no cover
spider = MagicMock(crawler=MagicMock(stats=MagicMock(inc_value=MagicMock()))) # pragma: no cover

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
