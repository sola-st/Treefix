from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy import signals # pragma: no cover
from scrapy.crawler import Crawler # pragma: no cover

crawler = type('MockCrawler', (object,), {'settings': {'LOGSTATS_INTERVAL': 0}, 'stats': {}, 'signals': signals})() # pragma: no cover
cls = type('MockClass', (object,), {'__init__': lambda self, stats, interval: None}) # pragma: no cover

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
