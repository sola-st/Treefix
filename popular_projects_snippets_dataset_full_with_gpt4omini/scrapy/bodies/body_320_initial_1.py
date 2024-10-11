import logging # pragma: no cover
class MockCrawler: pass # pragma: no cover
class MockSpider: pass # pragma: no cover
class MockRequestFingerprinter: pass # pragma: no cover

logger = logging.getLogger('test_logger') # pragma: no cover
self = type('Mock', (object,), {'cachedir': '/path/to/cache', '_fingerprinter': None})() # pragma: no cover
spider = type('Mock', (object,), {'crawler': type('MockCrawler', (object,), {'request_fingerprinter': MockRequestFingerprinter()})()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
from l3.Runtime import _l_
logger.debug("Using filesystem cache storage in %(cachedir)s", {'cachedir': self.cachedir},
             extra={'spider': spider})
_l_(7500)

self._fingerprinter = spider.crawler.request_fingerprinter
_l_(7501)
