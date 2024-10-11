from scrapy.signalmanager import SignalManager # pragma: no cover
from scrapy.crawler import Crawler # pragma: no cover

self = type('MockSelf', (object,), {'close': lambda: None})() # pragma: no cover
crawler = type('MockCrawler', (object,), {'settings': {}, 'signals': SignalManager()})() # pragma: no cover
signals = type('MockSignals', (object,), {'spider_closed': 'spider_closed_signal'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spiders/__init__.py
from l3.Runtime import _l_
self.crawler = crawler
_l_(7363)
self.settings = crawler.settings
_l_(7364)
crawler.signals.connect(self.close, signals.spider_closed)
_l_(7365)
