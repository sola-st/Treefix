from scrapy import signals # pragma: no cover
from scrapy.exceptions import NotConfigured # pragma: no cover

class MockSettings:  # Mock class for settings# pragma: no cover
    def getfloat(self, key):# pragma: no cover
        if key == 'LOGSTATS_INTERVAL':# pragma: no cover
            return 10.0  # example interval value# pragma: no cover
        return None# pragma: no cover
# pragma: no cover
class MockStats:  # Mock class for stats# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
class MockSignals:  # Mock class for signals# pragma: no cover
    def __init__(self):# pragma: no cover
        self._signals = {}# pragma: no cover
# pragma: no cover
    def connect(self, func, signal):# pragma: no cover
        self._signals[signal] = func# pragma: no cover
# pragma: no cover
class MockCrawler:  # Mock class for crawler# pragma: no cover
    def __init__(self):# pragma: no cover
        self.settings = MockSettings()# pragma: no cover
        self.stats = MockStats()# pragma: no cover
        self.signals = MockSignals()# pragma: no cover
# pragma: no cover
crawler = MockCrawler()  # Initialize the crawler# pragma: no cover
cls = object  # Use built-in object for cls # pragma: no cover

from scrapy import signals # pragma: no cover
from scrapy.exceptions import NotConfigured # pragma: no cover

class MockSettings:  # Mock class for settings# pragma: no cover
    def getfloat(self, key):# pragma: no cover
        if key == 'LOGSTATS_INTERVAL':# pragma: no cover
            return 10.0  # example interval value# pragma: no cover
        return None# pragma: no cover
# pragma: no cover
class MockStats:  # Mock class for stats# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
class MockSignals:  # Mock class for signals# pragma: no cover
    def __init__(self):# pragma: no cover
        self._signals = {}# pragma: no cover
# pragma: no cover
    def connect(self, func, signal):# pragma: no cover
        self._signals[signal] = func# pragma: no cover
# pragma: no cover
class MockObserver:  # Updated class to accept arguments# pragma: no cover
    def __init__(self, stats, interval):# pragma: no cover
        self.stats = stats  # Store stats# pragma: no cover
        self.interval = interval  # Store interval# pragma: no cover
    def spider_opened(self):# pragma: no cover
        print('Spider opened')# pragma: no cover
    def spider_closed(self):# pragma: no cover
        print('Spider closed')# pragma: no cover
# pragma: no cover
class MockCrawler:  # Mock class for crawler# pragma: no cover
    def __init__(self):# pragma: no cover
        self.settings = MockSettings()# pragma: no cover
        self.stats = MockStats()# pragma: no cover
        self.signals = MockSignals()# pragma: no cover
# pragma: no cover
crawler = MockCrawler()  # Initialize the crawler# pragma: no cover
cls = MockObserver  # Correct class for initialization # pragma: no cover

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
