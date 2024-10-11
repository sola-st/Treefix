from scrapy import signals # pragma: no cover
from scrapy.crawler import CrawlerProcess # pragma: no cover

class MockSettings: pass # pragma: no cover
class MockStats: pass # pragma: no cover
class MockSignals: pass # pragma: no cover
class MockCrawler:  # pragma: no cover
    def __init__(self):  # pragma: no cover
        self.settings = MockSettings()  # pragma: no cover
        self.stats = MockStats()  # pragma: no cover
        self.signals = MockSignals()  # pragma: no cover
crawler = MockCrawler() # pragma: no cover
cls = type('MockSpider', (), {}) # pragma: no cover
signals = MockSignals() # pragma: no cover

from scrapy import signals # pragma: no cover

class MockSettings: pass # pragma: no cover
class MockStats: pass # pragma: no cover
class MockSignals:  # pragma: no cover
    def connect(self, method, signal): pass # pragma: no cover
class MockSpider:  # pragma: no cover
    def __init__(self, settings, stats):  # pragma: no cover
        self.settings = settings  # pragma: no cover
        self.stats = stats  # pragma: no cover
crawler = type('MockCrawler', (), {'settings': MockSettings(), 'stats': MockStats(), 'signals': MockSignals()})() # pragma: no cover
cls = MockSpider # pragma: no cover
signals = MockSignals() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/httpcache.py
from l3.Runtime import _l_
o = cls(crawler.settings, crawler.stats)
_l_(6502)
crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
_l_(6503)
crawler.signals.connect(o.spider_closed, signal=signals.spider_closed)
_l_(6504)
aux = o
_l_(6505)
exit(aux)
