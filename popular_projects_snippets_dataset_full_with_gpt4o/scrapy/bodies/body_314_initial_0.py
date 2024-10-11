from pathlib import Path # pragma: no cover
import logging # pragma: no cover
type('Mock', (object,), {}) # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self.cachedir = '/tmp/cache' # pragma: no cover
spider = type('Mock', (object,), {'name': 'example_spider'})() # pragma: no cover
self.dbmodule = type('Mock', (object,), {'open': lambda dbpath, mode: f'DB opened at {dbpath} with mode {mode}'})() # pragma: no cover
logger = logging.getLogger('example_logger') # pragma: no cover
self._fingerprinter = 'example_fingerprinter' # pragma: no cover
spider.crawler = type('Mock', (object,), {'request_fingerprinter': self._fingerprinter})() # pragma: no cover

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
