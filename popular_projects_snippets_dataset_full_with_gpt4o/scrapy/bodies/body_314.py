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
