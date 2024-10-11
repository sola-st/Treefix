from unittest.mock import Mock # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
crawler = type('Mock', (object,), {'settings': {}, 'signals': type('Mock', (object,), {'connect': lambda x, y: None})()})() # pragma: no cover
signals = type('Mock', (object,), {'spider_closed': object})() # pragma: no cover
self.close = lambda spider: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/__init__.py
from l3.Runtime import _l_
self.crawler = crawler
_l_(18269)
self.settings = crawler.settings
_l_(18270)
crawler.signals.connect(self.close, signals.spider_closed)
_l_(18271)
