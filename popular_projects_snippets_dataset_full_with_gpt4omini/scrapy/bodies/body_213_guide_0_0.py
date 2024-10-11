from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy import signals # pragma: no cover

class MockStats(object): # pragma: no cover
    def __init__(self): # pragma: no cover
        pass # pragma: no cover
mock_stats = MockStats() # pragma: no cover
class MockCrawler(object): # pragma: no cover
    def __init__(self): # pragma: no cover
        self.stats = mock_stats # pragma: no cover
        self.settings = {'LOGSTATS_INTERVAL': 0.0} # pragma: no cover
    def signals(self): # pragma: no cover
        pass # pragma: no cover
crawler = MockCrawler() # pragma: no cover
class Mock(object): # pragma: no cover
    def __init__(self, stats, interval): # pragma: no cover
        self.stats = stats # pragma: no cover
        self.interval = interval # pragma: no cover
cls = Mock # pragma: no cover

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
