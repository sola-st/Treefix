from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy import signals # pragma: no cover

class MockCrawler: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.settings = MockSettings() # pragma: no cover
        self.stats = MockStats() # pragma: no cover
        self.signals = type('Mock', (object,), {'connect': lambda self, func, signal=None: None})() # pragma: no cover
 # pragma: no cover
class MockSettings: # pragma: no cover
    def getfloat(self, key): # pragma: no cover
        return 0.0  # Set to 0.0 to execute the uncovered paths # pragma: no cover
 # pragma: no cover
class MockStats: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
crawler = MockCrawler() # pragma: no cover
cls = lambda stats, interval: type('Mock', (object,), dict(spider_opened=lambda self: None, spider_closed=lambda self: None)) # pragma: no cover

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
