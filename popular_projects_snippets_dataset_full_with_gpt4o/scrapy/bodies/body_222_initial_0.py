from collections import defaultdict # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = Mock() # pragma: no cover
spider = Mock() # pragma: no cover
self.counter = defaultdict(int) # pragma: no cover
self.close_on = {'itemcount': 5} # pragma: no cover
self.crawler = Mock() # pragma: no cover
self.crawler.engine = Mock() # pragma: no cover
self.crawler.engine.close_spider = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/closespider.py
from l3.Runtime import _l_
self.counter['itemcount'] += 1
_l_(18671)
if self.counter['itemcount'] == self.close_on['itemcount']:
    _l_(18673)

    self.crawler.engine.close_spider(spider, 'closespider_itemcount')
    _l_(18672)
