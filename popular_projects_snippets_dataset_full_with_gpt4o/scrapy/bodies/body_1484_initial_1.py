from types import SimpleNamespace # pragma: no cover
import logging # pragma: no cover

request = SimpleNamespace(url='https://example.com/some/very/long/path/to/resource') # pragma: no cover
Request = type('Request', (object,), {}) # pragma: no cover
self = SimpleNamespace(maxlength=50) # pragma: no cover
logger = logging.getLogger('example_logger') # pragma: no cover
spider = SimpleNamespace(crawler=SimpleNamespace(stats=SimpleNamespace(inc_value=lambda *args, **kwargs: None))) # pragma: no cover

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
