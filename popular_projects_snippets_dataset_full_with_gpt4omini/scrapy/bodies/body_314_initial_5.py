from pathlib import Path # pragma: no cover
import logging # pragma: no cover
import dbm # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.cachedir = '/tmp/cache' # pragma: no cover
self.dbmodule = dbm # pragma: no cover
spider = Mock() # pragma: no cover
spider.name = 'example_spider' # pragma: no cover
spider.crawler = Mock() # pragma: no cover
spider.crawler.request_fingerprinter = 'fingerprinter_object' # pragma: no cover
logger = logging.getLogger('example_logger') # pragma: no cover

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
