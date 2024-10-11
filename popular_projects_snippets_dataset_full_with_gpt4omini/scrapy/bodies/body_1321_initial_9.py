from scrapy.crawler import Crawler # pragma: no cover
from scrapy import signals # pragma: no cover
from scrapy.statscollectors import StatsCollector # pragma: no cover
from scrapy.signalmanager import SignalManager # pragma: no cover

class MockCrawler:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.settings = {}# pragma: no cover
        self.signals = SignalManager(self)# pragma: no cover
# pragma: no cover
crawler = MockCrawler() # pragma: no cover
cls = type('MockClass', (object,), {}) # pragma: no cover
signals = signals # pragma: no cover

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
