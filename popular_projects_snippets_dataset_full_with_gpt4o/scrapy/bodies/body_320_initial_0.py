import logging # pragma: no cover

logger = logging.getLogger('example') # pragma: no cover
self = type('Mock', (object,), {'cachedir': '/path/to/cache/dir', '_fingerprinter': None})() # pragma: no cover
spider = type('Mock', (object,), {'crawler': type('Mock', (object,), {'request_fingerprinter': 'fingerprinter_value'})()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
from l3.Runtime import _l_
logger.debug("Using filesystem cache storage in %(cachedir)s", {'cachedir': self.cachedir},
             extra={'spider': spider})
_l_(18403)

self._fingerprinter = spider.crawler.request_fingerprinter
_l_(18404)
