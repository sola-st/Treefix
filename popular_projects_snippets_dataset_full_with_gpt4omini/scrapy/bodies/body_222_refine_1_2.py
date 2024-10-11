from scrapy.crawler import CrawlerProcess # pragma: no cover

spider = 'mock_spider' # pragma: no cover

from scrapy.crawler import CrawlerProcess # pragma: no cover

class MockSpider:  # Dummy class to simulate the spider # pragma: no cover
    def __init__(self): # pragma: no cover
        self.counter = {'itemcount': 0} # pragma: no cover
        self.close_on = {'itemcount': 1} # pragma: no cover
        self.crawler = type('MockCrawler', (object,), {'engine': type('MockEngine', (object,), {'close_spider': lambda self, spider, reason: print(f'Spider closed: {reason}')})()})() # pragma: no cover
spider = MockSpider() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/closespider.py
from l3.Runtime import _l_
self.counter['itemcount'] += 1
_l_(7824)
if self.counter['itemcount'] == self.close_on['itemcount']:
    _l_(7826)

    self.crawler.engine.close_spider(spider, 'closespider_itemcount')
    _l_(7825)
