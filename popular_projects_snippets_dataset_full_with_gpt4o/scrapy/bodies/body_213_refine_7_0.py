from scrapy.exceptions import NotConfigured # pragma: no cover

crawler = type('Mock', (object,), {'settings': type('Mock', (object,), {'getfloat': lambda x: 5.0})(), 'stats': type('Mock', (object,), {})(), 'signals': type('Mock', (object,), {'connect': lambda x, signal: None})()})() # pragma: no cover
cls = lambda stats, interval: type('Mock', (object,), {'spider_opened': lambda self: None, 'spider_closed': lambda self: None})() # pragma: no cover
signals = type('Mock', (object,), {'spider_opened': object(), 'spider_closed': object()})() # pragma: no cover

from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy import signals # pragma: no cover

crawler = type('Mock', (object,), {# pragma: no cover
    'settings': type('MockSettings', (object,), {'getfloat': lambda self, key: 5.0})(),# pragma: no cover
    'stats': type('MockStats', (object,), {})(),# pragma: no cover
    'signals': type('MockSignals', (object,), {'connect': lambda self, handler, signal: None})()# pragma: no cover
 })() # pragma: no cover
NotConfigured = NotConfigured # pragma: no cover
cls = type('MockClass', (object,), {# pragma: no cover
    '__init__': lambda self, stats, interval: None,# pragma: no cover
    'spider_opened': lambda self, spider: None,# pragma: no cover
    'spider_closed': lambda self, spider: None# pragma: no cover
}) # pragma: no cover
signals = type('MockSignalsEnum', (object,), {# pragma: no cover
    'spider_opened': 'spider_opened_signal',# pragma: no cover
    'spider_closed': 'spider_closed_signal'# pragma: no cover
})() # pragma: no cover

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
