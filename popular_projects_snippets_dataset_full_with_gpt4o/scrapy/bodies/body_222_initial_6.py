self = type('Mock', (object,), {# pragma: no cover
    'counter': {'itemcount': 0},# pragma: no cover
    'close_on': {'itemcount': 10},# pragma: no cover
    'crawler': type('CrawlerMock', (object,), {'engine': type('EngineMock', (object,), {'close_spider': lambda spider, reason: None})()})()})() # pragma: no cover
spider = 'example_spider' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/closespider.py
from l3.Runtime import _l_
self.counter['itemcount'] += 1
_l_(18671)
if self.counter['itemcount'] == self.close_on['itemcount']:
    _l_(18673)

    self.crawler.engine.close_spider(spider, 'closespider_itemcount')
    _l_(18672)
