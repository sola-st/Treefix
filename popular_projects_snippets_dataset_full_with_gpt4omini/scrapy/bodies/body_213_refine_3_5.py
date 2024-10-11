from scrapy import signals # pragma: no cover
from scrapy.exceptions import NotConfigured # pragma: no cover

class MockCrawler:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.settings = {'LOGSTATS_INTERVAL': 10.0}# pragma: no cover
        self.stats = {}# pragma: no cover
# pragma: no cover
crawler = MockCrawler() # pragma: no cover
class NotConfigured(Exception):# pragma: no cover
    pass # pragma: no cover
def cls(stats, interval):# pragma: no cover
    return {'stats': stats, 'interval': interval} # pragma: no cover

from scrapy import signals # pragma: no cover
from scrapy.exceptions import NotConfigured # pragma: no cover

class MockSettings:# pragma: no cover
    def getfloat(self, key):# pragma: no cover
        if key == 'LOGSTATS_INTERVAL':# pragma: no cover
            return 10.0# pragma: no cover
        raise KeyError(f'Key {key} not found')# pragma: no cover
# pragma: no cover
class MockCrawler:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.settings = MockSettings()# pragma: no cover
        self.stats = {}# pragma: no cover
# pragma: no cover
crawler = MockCrawler() # pragma: no cover
NotConfigured = Exception('NotConfigured') # pragma: no cover
def cls(stats, interval):# pragma: no cover
    return {'stats': stats, 'interval': interval}# pragma: no cover
# pragma: no cover
# Create an instance of cls for the initial call# pragma: no cover
instance = cls(crawler.stats, crawler.settings.getfloat('LOGSTATS_INTERVAL')) # pragma: no cover

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
