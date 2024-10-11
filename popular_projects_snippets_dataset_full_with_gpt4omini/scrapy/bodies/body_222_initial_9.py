from scrapy.crawler import Crawler # pragma: no cover

self = type('MockSelf', (), {'counter': {'itemcount': 0}, 'close_on': {'itemcount': 5}, 'crawler': type('MockCrawler', (), {'engine': type('MockEngine', (), {'close_spider': lambda self, spider, reason: print(f'Spider {spider} closed due to {reason}')})()})()})() # pragma: no cover
spider = 'test_spider' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/closespider.py
from l3.Runtime import _l_
self.counter['itemcount'] += 1
_l_(7824)
if self.counter['itemcount'] == self.close_on['itemcount']:
    _l_(7826)

    self.crawler.engine.close_spider(spider, 'closespider_itemcount')
    _l_(7825)
