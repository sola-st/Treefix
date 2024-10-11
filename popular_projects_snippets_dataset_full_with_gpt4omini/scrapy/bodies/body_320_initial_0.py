class MockSpider: pass # pragma: no cover
spider = MockSpider() # pragma: no cover
self = type('MockSelf', (), {'cachedir': '/path/to/cache', '_fingerprinter': None})() # pragma: no cover
self._fingerprinter = type('MockFingerprinter', (), {})() # pragma: no cover
spider.crawler = type('MockCrawler', (), {})() # pragma: no cover
spider.crawler.request_fingerprinter = type('MockRequestFingerprinter', (), {})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
from l3.Runtime import _l_
logger.debug("Using filesystem cache storage in %(cachedir)s", {'cachedir': self.cachedir},
             extra={'spider': spider})
_l_(7500)

self._fingerprinter = spider.crawler.request_fingerprinter
_l_(7501)
