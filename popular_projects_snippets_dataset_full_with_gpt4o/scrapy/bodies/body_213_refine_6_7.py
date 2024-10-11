from unittest.mock import Mock # pragma: no cover
from scrapy.exceptions import NotConfigured # pragma: no cover

crawler = Mock() # pragma: no cover
NotConfigured = NotConfigured # pragma: no cover
cls = Mock() # pragma: no cover
signals = type('Mock', (object,), {'spider_opened': 'spider_opened', 'spider_closed': 'spider_closed'}) # pragma: no cover
crawler.settings = Mock(getfloat=Mock(return_value=5.0)) # pragma: no cover
crawler.stats = Mock() # pragma: no cover
crawler.signals = Mock(connect=Mock()) # pragma: no cover

from unittest.mock import Mock, MagicMock # pragma: no cover
from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy import signals # pragma: no cover

crawler = type('CrawlerMock', (object,), {'settings': MagicMock(getfloat=lambda key: 5.0), 'stats': Mock(), 'signals': Mock(connect=Mock())})() # pragma: no cover
NotConfigured = NotConfigured # pragma: no cover
cls = type('MyClass', (object,), {'__init__': lambda self, stats, interval: None, 'spider_opened': lambda self, spider: None, 'spider_closed': lambda self, reason: None}) # pragma: no cover
signals = type('SignalsMock', (object,), {'spider_opened': 'spider_opened_signal', 'spider_closed': 'spider_closed_signal'})() # pragma: no cover

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
