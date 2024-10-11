from scrapy import signals # pragma: no cover
from scrapy.crawler import Crawler # pragma: no cover
from scrapy.statscollectors import StatsCollector # pragma: no cover

class MockSettings:# pragma: no cover
    def __init__(self):# pragma: no cover
        pass# pragma: no cover
settings = MockSettings() # pragma: no cover
class MockStats:# pragma: no cover
    def __init__(self):# pragma: no cover
        pass# pragma: no cover
stats = MockStats() # pragma: no cover
class MockSignals:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.connections = {}# pragma: no cover
    def connect(self, callback, signal):# pragma: no cover
        self.connections[signal] = callback# pragma: no cover
signals = MockSignals() # pragma: no cover
class MockCrawler:# pragma: no cover
    def __init__(self, settings, stats):# pragma: no cover
        self.settings = settings# pragma: no cover
        self.stats = stats# pragma: no cover
        self.signals = signals# pragma: no cover
crawler = MockCrawler(settings, stats) # pragma: no cover
class MockClass:# pragma: no cover
    def __init__(self, settings, stats):# pragma: no cover
        pass# pragma: no cover
cls = MockClass # pragma: no cover

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
