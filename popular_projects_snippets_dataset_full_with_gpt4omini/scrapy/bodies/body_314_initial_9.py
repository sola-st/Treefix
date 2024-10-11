from pathlib import Path # pragma: no cover
import logging # pragma: no cover
import sqlite3 # pragma: no cover

self = type('Mock', (), {'cachedir': '/tmp'})() # pragma: no cover
spider = type('Mock', (), {'name': 'example_spider', 'crawler': type('Mock', (), {'request_fingerprinter': 'fingerprinter'})()})() # pragma: no cover
logger = logging.getLogger('test_logger') # pragma: no cover
self.dbmodule = sqlite3 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
from l3.Runtime import _l_
dbpath = Path(self.cachedir, f'{spider.name}.db')
_l_(8221)
self.db = self.dbmodule.open(str(dbpath), 'c')
_l_(8222)

logger.debug("Using DBM cache storage in %(cachepath)s", {'cachepath': dbpath}, extra={'spider': spider})
_l_(8223)

self._fingerprinter = spider.crawler.request_fingerprinter
_l_(8224)
