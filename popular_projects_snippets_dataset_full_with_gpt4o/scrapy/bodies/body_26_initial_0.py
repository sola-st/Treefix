self = type('Mock', (object,), {'spider_stats': {}})() # pragma: no cover
spider = type('Mock', (object,), {'name': 'example_spider'})() # pragma: no cover
stats = {'pages_crawled': 10, 'items_scraped': 5} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/statscollectors.py
from l3.Runtime import _l_
self.spider_stats[spider.name] = stats
_l_(21115)
