from unittest.mock import Mock # pragma: no cover
import scrapy # pragma: no cover

cls = Mock() # pragma: no cover
crawler = type('MockCrawler', (object,), {'settings': Mock(), 'stats': Mock(), 'signals': Mock()})() # pragma: no cover
signals = type('MockSignals', (object,), {'spider_opened': Mock(), 'spider_closed': Mock()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/httpcache.py
from l3.Runtime import _l_
o = cls(crawler.settings, crawler.stats)
_l_(17725)
crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
_l_(17726)
crawler.signals.connect(o.spider_closed, signal=signals.spider_closed)
_l_(17727)
aux = o
_l_(17728)
exit(aux)
