from pathlib import Path # pragma: no cover
import logging # pragma: no cover

self = type('MockSelf', (object,), {})() # pragma: no cover
self.cachedir = '/path/to/cache' # pragma: no cover
spider = type('MockSpider', (object,), {})() # pragma: no cover
spider.name = 'example_spider' # pragma: no cover
self.dbmodule = type('MockDBModule', (object,), {'open': lambda *args: 'db_object'})() # pragma: no cover
logger = logging.getLogger('test_logger') # pragma: no cover
spider.crawler = type('MockCrawler', (object,), {})() # pragma: no cover
spider.crawler.request_fingerprinter = 'fingerprinter_object' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
from l3.Runtime import _l_
dbpath = Path(self.cachedir, f'{spider.name}.db')
_l_(19425)
self.db = self.dbmodule.open(str(dbpath), 'c')
_l_(19426)

logger.debug("Using DBM cache storage in %(cachepath)s", {'cachepath': dbpath}, extra={'spider': spider})
_l_(19427)

self._fingerprinter = spider.crawler.request_fingerprinter
_l_(19428)
