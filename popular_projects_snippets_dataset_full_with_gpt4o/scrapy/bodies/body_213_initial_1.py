from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy import signals # pragma: no cover

crawler = type('Mock', (object,), {'settings': type('Settings', (object,), {'getfloat': lambda self, key: 5.0})(), 'stats': object(), 'signals': type('Signals', (object,), {'connect': lambda self, callback, signal: None})()})() # pragma: no cover
NotConfigured = NotConfigured # pragma: no cover
cls = lambda stats, interval: type('SpiderObject', (object,), {'spider_opened': lambda self: None, 'spider_closed': lambda self: None})() # pragma: no cover
signals = type('MockSignals', (object,), {'spider_opened': object, 'spider_closed': object}) # pragma: no cover

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
