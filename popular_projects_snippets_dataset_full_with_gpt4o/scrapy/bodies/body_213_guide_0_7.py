from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy import signals # pragma: no cover

class MockCrawlerSettings: # pragma: no cover
    @staticmethod # pragma: no cover
    def getfloat(arg): # pragma: no cover
        return None  # This should be None to trigger the uncovered path # pragma: no cover
 # pragma: no cover
class MockCrawlerStats: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class MockCrawlerSignals: # pragma: no cover
    def connect(self, *args, **kwargs): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class MockCrawler: # pragma: no cover
    settings = MockCrawlerSettings() # pragma: no cover
    stats = MockCrawlerStats() # pragma: no cover
    signals = MockCrawlerSignals() # pragma: no cover
 # pragma: no cover
crawler = MockCrawler() # pragma: no cover
 # pragma: no cover
class MockObj: # pragma: no cover
    def spider_opened(self): # pragma: no cover
        pass # pragma: no cover
    def spider_closed(self): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
cls = MockObj # pragma: no cover

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
