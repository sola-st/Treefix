from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy import signals # pragma: no cover

class MockStats: pass # pragma: no cover
class MockSettings:  # Mock settings to return None for LOGSTATS_INTERVAL # pragma: no cover
    def getfloat(self, key): # pragma: no cover
        if key == 'LOGSTATS_INTERVAL': return None # pragma: no cover
        return 0.0 # pragma: no cover
class MockSignals:  # Mock signals class that does not implement real logic # pragma: no cover
    def connect(self, callback, signal): pass # pragma: no cover
class MockCrawler:  # Mock crawler structure # pragma: no cover
    def __init__(self): # pragma: no cover
        self.settings = MockSettings() # pragma: no cover
        self.stats = MockStats() # pragma: no cover
        self.signals = MockSignals() # pragma: no cover
crawler = MockCrawler() # pragma: no cover
class MockClass:  # Mock class with methods # pragma: no cover
    def __init__(self, stats, interval): pass # pragma: no cover
    def spider_opened(self): pass # pragma: no cover
    def spider_closed(self): pass # pragma: no cover
cls = MockClass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/logstats.py
from l3.Runtime import _l_
interval = crawler.settings.getfloat('LOGSTATS_INTERVAL')
_l_(5759)
if not interval:
    _l_(5761)

    raise NotConfigured
    _l_(5760)
o = cls(crawler.stats, interval)
_l_(5762)
crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
_l_(5763)
crawler.signals.connect(o.spider_closed, signal=signals.spider_closed)
_l_(5764)
aux = o
_l_(5765)
exit(aux)
