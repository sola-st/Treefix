from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy import signals # pragma: no cover

crawler = type('MockCrawler', (object,), {'settings': type('MockSettings', (object,), {'getfloat': lambda self, key: 5.0})(), 'stats': type('MockStats', (object,), {})(), 'signals': type('MockSignals', (object,), {'connect': lambda self, func, signal: None})()})() # pragma: no cover
NotConfigured = NotConfigured # pragma: no cover
cls = type('MockCls', (object,), {'__init__': lambda self, stats, interval: None, 'spider_opened': lambda self: None, 'spider_closed': lambda self: None}) # pragma: no cover
signals = type('MockSignals', (object,), {'spider_opened': 'spider_opened_signal', 'spider_closed': 'spider_closed_signal'})() # pragma: no cover

from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy import signals # pragma: no cover

class MockCrawler: # pragma: no cover
    class Settings: # pragma: no cover
        @staticmethod # pragma: no cover
        def getfloat(name): # pragma: no cover
            return 5.0 # pragma: no cover
    class Signals: # pragma: no cover
        @staticmethod # pragma: no cover
        def connect(handler, signal): # pragma: no cover
            pass # pragma: no cover
    settings = Settings() # pragma: no cover
    stats = object() # pragma: no cover
    signals = Signals() # pragma: no cover
crawler = MockCrawler() # pragma: no cover
class MockCls: # pragma: no cover
    def __init__(self, stats, interval): # pragma: no cover
        pass # pragma: no cover
    def spider_opened(self): # pragma: no cover
        pass # pragma: no cover
    def spider_closed(self): # pragma: no cover
        pass # pragma: no cover
cls = MockCls # pragma: no cover
class MockSignals: # pragma: no cover
    spider_opened = 'spider_opened' # pragma: no cover
    spider_closed = 'spider_closed' # pragma: no cover
signals = MockSignals # pragma: no cover

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
