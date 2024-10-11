from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy import signals # pragma: no cover
import scrapy # pragma: no cover

class MockStats(object): # pragma: no cover
    def __init__(self): # pragma: no cover
        self.data = {} # pragma: no cover
    def get(self, key, default=None): # pragma: no cover
        return self.data.get(key, default) # pragma: no cover
    def set(self, key, value): # pragma: no cover
        self.data[key] = value # pragma: no cover
class MockCrawler(object): # pragma: no cover
    def __init__(self): # pragma: no cover
        self.stats = MockStats() # pragma: no cover
        self.settings = {'LOGSTATS_INTERVAL': 0.0} # pragma: no cover
crawler = MockCrawler() # pragma: no cover
interval = crawler.settings['LOGSTATS_INTERVAL'] # pragma: no cover
cls = type('MockClass', (), {}) # pragma: no cover

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
