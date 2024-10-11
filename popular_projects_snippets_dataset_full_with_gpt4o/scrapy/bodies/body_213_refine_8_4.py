from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy import signals # pragma: no cover

crawler = type('MockCrawler', (object,), {'settings': type('MockSettings', (object,), {'getfloat': lambda self, key: 5.0})(), 'stats': type('MockStats', (object,), {})(), 'signals': type('MockSignals', (object,), {'connect': lambda self, func, signal: None})()})() # pragma: no cover
NotConfigured = NotConfigured # pragma: no cover
cls = type('MockCls', (object,), {'__init__': lambda self, stats, interval: None, 'spider_opened': lambda self: None, 'spider_closed': lambda self: None}) # pragma: no cover
signals = type('MockSignals', (object,), {'spider_opened': 'spider_opened_signal', 'spider_closed': 'spider_closed_signal'})() # pragma: no cover

from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy import signals # pragma: no cover

class MockCrawlerSettings:# pragma: no cover
    def getfloat(self, key):# pragma: no cover
        return 5.0 # pragma: no cover
class MockCrawlerSignals:# pragma: no cover
    def connect(self, func, signal):# pragma: no cover
        pass # pragma: no cover
class MockCrawler:# pragma: no cover
    settings = MockCrawlerSettings()# pragma: no cover
    stats = object()# pragma: no cover
    signals = MockCrawlerSignals() # pragma: no cover
crawler = MockCrawler() # pragma: no cover
NotConfigured = NotConfigured # pragma: no cover
class MockCls:# pragma: no cover
    def __init__(self, stats, interval):# pragma: no cover
        self.stats = stats# pragma: no cover
        self.interval = interval# pragma: no cover
    def spider_opened(self):# pragma: no cover
        pass# pragma: no cover
    def spider_closed(self):# pragma: no cover
        pass # pragma: no cover
cls = MockCls # pragma: no cover
signals = type('MockSignals', (object,), {'spider_opened': 'spider_opened', 'spider_closed': 'spider_closed'}) # pragma: no cover

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
