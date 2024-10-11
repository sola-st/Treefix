from scrapy import signals # pragma: no cover
from scrapy.signalmanager import dispatcher # pragma: no cover

class MockCrawler: settings = {'USER_AGENT': 'my-user-agent'}; stats = { 'start_time': '2023-10-01T00:00:00Z' }; signals = dispatcher # pragma: no cover
class Mock: pass # pragma: no cover
cls = Mock # pragma: no cover
crawler = MockCrawler() # pragma: no cover
signals = signals # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/httpcache.py
from l3.Runtime import _l_
o = cls(crawler.settings, crawler.stats)
_l_(6502)
crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
_l_(6503)
crawler.signals.connect(o.spider_closed, signal=signals.spider_closed)
_l_(6504)
aux = o
_l_(6505)
exit(aux)
