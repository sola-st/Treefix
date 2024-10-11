from scrapy import Spider # pragma: no cover

from scrapy.spiders import Spider # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/closespider.py
from l3.Runtime import _l_
self.counter['itemcount'] += 1
_l_(7824)
if self.counter['itemcount'] == self.close_on['itemcount']:
    _l_(7826)

    self.crawler.engine.close_spider(spider, 'closespider_itemcount')
    _l_(7825)
