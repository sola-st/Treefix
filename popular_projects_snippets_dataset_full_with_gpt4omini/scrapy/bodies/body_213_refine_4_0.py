from scrapy import signals # pragma: no cover
from scrapy.exceptions import NotConfigured # pragma: no cover

class MockSettings:# pragma: no cover
    def getfloat(self, name):# pragma: no cover
        return 5.0  # Sample interval# pragma: no cover
# pragma: no cover
class MockStats:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
class MockSignals:# pragma: no cover
    def connect(self, func, signal):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
class MockCrawler:# pragma: no cover
    settings = MockSettings()# pragma: no cover
    stats = MockStats()# pragma: no cover
    signals = MockSignals()# pragma: no cover
# pragma: no cover
crawler = MockCrawler() # pragma: no cover
class NotConfigured(Exception):# pragma: no cover
    pass # pragma: no cover
class MockCls:# pragma: no cover
    def __init__(self, stats, interval):# pragma: no cover
        self.stats = stats# pragma: no cover
        self.interval = interval# pragma: no cover
    def spider_opened(self):# pragma: no cover
        pass# pragma: no cover
    def spider_closed(self):# pragma: no cover
        pass# pragma: no cover
cls = MockCls # pragma: no cover
signals = signals # pragma: no cover

from scrapy import signals # pragma: no cover
from scrapy.exceptions import NotConfigured # pragma: no cover

class MockSettings:# pragma: no cover
    def getfloat(self, name):# pragma: no cover
        return 5.0  # Sample interval# pragma: no cover
# pragma: no cover
class MockStats:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
class MockSignals:# pragma: no cover
    def connect(self, func, signal):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
class MockCrawler:# pragma: no cover
    settings = MockSettings()# pragma: no cover
    stats = MockStats()# pragma: no cover
    signals = MockSignals()# pragma: no cover
# pragma: no cover
crawler = MockCrawler() # pragma: no cover
class NotConfigured(Exception):# pragma: no cover
    pass # pragma: no cover
class MockCls:# pragma: no cover
    def __init__(self, stats, interval):# pragma: no cover
        self.stats = stats# pragma: no cover
        self.interval = interval# pragma: no cover
    def spider_opened(self):# pragma: no cover
        print('Spider opened')# pragma: no cover
    def spider_closed(self):# pragma: no cover
        print('Spider closed')# pragma: no cover
# pragma: no cover
cls = MockCls # pragma: no cover
signals = MockSignals() # pragma: no cover

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
