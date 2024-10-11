from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy import signals # pragma: no cover

crawler = type('Mock', (object,), {'settings': type('Settings', (object,), {'getfloat': lambda self, key: 5.0})(), 'stats': object(), 'signals': type('Signals', (object,), {'connect': lambda self, callback, signal: None})()})() # pragma: no cover
NotConfigured = NotConfigured # pragma: no cover
cls = lambda stats, interval: type('SpiderObject', (object,), {'spider_opened': lambda self: None, 'spider_closed': lambda self: None})() # pragma: no cover
signals = type('MockSignals', (object,), {'spider_opened': object, 'spider_closed': object}) # pragma: no cover

from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy import signals # pragma: no cover
import sys # pragma: no cover

class MockSignalManager: # pragma: no cover
    def connect(self, callback, signal): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class MockSettings: # pragma: no cover
    def getfloat(self, key): # pragma: no cover
        return 5.0 # pragma: no cover
 # pragma: no cover
class MockCrawler: # pragma: no cover
    settings = MockSettings() # pragma: no cover
    stats = object() # pragma: no cover
    signals = MockSignalManager() # pragma: no cover
 # pragma: no cover
crawler = MockCrawler() # pragma: no cover
 # pragma: no cover
class SpiderObject: # pragma: no cover
    def __init__(self, stats, interval): # pragma: no cover
        pass # pragma: no cover
    def spider_opened(self): # pragma: no cover
        pass # pragma: no cover
    def spider_closed(self): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
cls = SpiderObject # pragma: no cover
signals = signals # pragma: no cover
 # pragma: no cover
NotConfigured = NotConfigured # pragma: no cover
 # pragma: no cover

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
