from collections import defaultdict # pragma: no cover

self = type('Mock', (object,), {'spider_stats': defaultdict(dict)})() # pragma: no cover
spider = type('Mock', (object,), {'name': 'example_spider'})() # pragma: no cover
stats = {'requests_made': 100, 'success_count': 95, 'failure_count': 5} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/statscollectors.py
from l3.Runtime import _l_
self.spider_stats[spider.name] = stats
_l_(9882)
