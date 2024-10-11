from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy import signals # pragma: no cover
class MockCrawler: # pragma: no cover
    class Settings: # pragma: no cover
        @staticmethod # pragma: no cover
        def getfloat(key): # pragma: no cover
            return None  # Simulate the getfloat method returning None for the test # pragma: no cover
 # pragma: no cover
    class Stats: # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
    def __init__(self): # pragma: no cover
        self.settings = self.Settings() # pragma: no cover
        self.stats = self.Stats() # pragma: no cover
        self.signals = self # pragma: no cover
         # pragma: no cover
    def connect(self, method, signal=None): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class MockStatsCollector: # pragma: no cover
    def __init__(self, stats, interval): # pragma: no cover
        self.stats = stats # pragma: no cover
        self.interval = interval # pragma: no cover
         # pragma: no cover
    def spider_opened(self): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
    def spider_closed(self): # pragma: no cover
        pass # pragma: no cover

crawler = MockCrawler() # pragma: no cover
cls = MockStatsCollector # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/logstats.py
from l3.Runtime import _l_
interval = crawler.settings.getfloat('LOGSTATS_INTERVAL')
_l_(16577)
if not interval:
    _l_(16579)

    raise NotConfigured
    _l_(16578)
o = cls(crawler.stats, interval)
_l_(16580)
crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
_l_(16581)
crawler.signals.connect(o.spider_closed, signal=signals.spider_closed)
_l_(16582)
aux = o
_l_(16583)
exit(aux)
