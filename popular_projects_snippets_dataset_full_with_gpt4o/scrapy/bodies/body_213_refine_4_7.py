from unittest.mock import Mock # pragma: no cover
from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy import signals # pragma: no cover

crawler = Mock() # pragma: no cover
crawler.settings = Mock() # pragma: no cover
crawler.stats = Mock() # pragma: no cover
crawler.signals = Mock() # pragma: no cover
NotConfigured = NotConfigured # pragma: no cover
cls = Mock() # pragma: no cover
signals.spider_opened = signals.spider_opened # pragma: no cover
signals.spider_closed = signals.spider_closed # pragma: no cover
crawler.settings.getfloat = Mock(return_value=1.0) # pragma: no cover

from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy import signals # pragma: no cover

crawler = type('MockCrawler', (object,), {# pragma: no cover
    'settings': type('MockSettings', (object,), {'getfloat': lambda self, name: 10.0})(),# pragma: no cover
    'stats': object(),# pragma: no cover
    'signals': type('MockSignals', (object,), {'connect': lambda self, func, signal: None})()# pragma: no cover
})() # pragma: no cover
NotConfigured = type('MockNotConfigured', (Exception,), {}) # pragma: no cover
cls = type('MockClass', (object,), {# pragma: no cover
    '__init__': lambda self, stats, interval: None,# pragma: no cover
    'spider_opened': lambda self, spider: None,# pragma: no cover
    'spider_closed': lambda self, spider: None# pragma: no cover
}) # pragma: no cover
signals = type('MockSignals', (object,), {# pragma: no cover
    'spider_opened': object(),# pragma: no cover
    'spider_closed': object()# pragma: no cover
}) # pragma: no cover

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
