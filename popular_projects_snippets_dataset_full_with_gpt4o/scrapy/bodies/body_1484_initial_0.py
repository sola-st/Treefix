from collections import namedtuple # pragma: no cover
import logging # pragma: no cover

Request = namedtuple('Request', ['url']) # pragma: no cover
request = Request(url='https://example.com/some-very-long-url-path') # pragma: no cover
self = type('Self', (object,), {'maxlength': 50})() # pragma: no cover
logger = logging.getLogger('example_logger') # pragma: no cover
logging.basicConfig(level=logging.INFO) # pragma: no cover
spider = type('Spider', (object,), {'crawler': type('Crawler', (object,), {'stats': type('Stats', (object,), {'inc_value': lambda self, key, spider: None})()})()})() # pragma: no cover

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
