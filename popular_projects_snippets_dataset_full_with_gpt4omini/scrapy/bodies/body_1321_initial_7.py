from scrapy import signals # pragma: no cover
from scrapy.crawler import Crawler # pragma: no cover
from scrapy.signalmanager import SignalManager # pragma: no cover

class MockSettings: pass # pragma: no cover
class MockStats: pass # pragma: no cover
class MockSignals: pass # pragma: no cover
crawler = type('MockCrawler', (object,), {'settings': MockSettings(), 'stats': MockStats(), 'signals': MockSignals()})() # pragma: no cover
signals = MockSignals() # pragma: no cover
cls = type('MockClass', (object,), {'__init__': lambda self, settings, stats: None}) # pragma: no cover

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
