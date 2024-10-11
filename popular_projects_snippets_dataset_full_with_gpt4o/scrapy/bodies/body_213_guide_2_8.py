from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy import signals # pragma: no cover

class Settings: # pragma: no cover
    def getfloat(self, name): # pragma: no cover
        return None  # Return None to trigger the NotConfigured exception # pragma: no cover
 # pragma: no cover
class Stats: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class SignalManager: # pragma: no cover
    def connect(self, func, signal): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class Crawler: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.settings = Settings() # pragma: no cover
        self.stats = Stats() # pragma: no cover
        self.signals = SignalManager() # pragma: no cover
 # pragma: no cover
class MockClass: # pragma: no cover
    def __init__(self, stats, interval): # pragma: no cover
        pass # pragma: no cover
    def spider_opened(self): # pragma: no cover
        pass # pragma: no cover
    def spider_closed(self): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
crawler = Crawler() # pragma: no cover
cls = MockClass # pragma: no cover

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
