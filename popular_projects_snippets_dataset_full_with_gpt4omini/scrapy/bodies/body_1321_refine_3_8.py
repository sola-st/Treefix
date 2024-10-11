from scrapy import signals # pragma: no cover
from scrapy.crawler import CrawlerProcess # pragma: no cover

class MockSignals(object): # pragma: no cover
    def connect(self, method, signal): pass; # pragma: no cover
signals = MockSignals() # pragma: no cover
class MockCls(object): # pragma: no cover
    def __init__(self, settings, stats): # pragma: no cover
        self.settings = settings # pragma: no cover
        self.stats = stats # pragma: no cover
    def spider_opened(self): pass # pragma: no cover
    def spider_closed(self): pass # pragma: no cover
cls = MockCls # pragma: no cover

from scrapy import signals # pragma: no cover
from scrapy.crawler import CrawlerProcess # pragma: no cover

class MockSettings(object):# pragma: no cover
    def __init__(self):# pragma: no cover
        self.settings = {'USER_AGENT': 'my-user-agent'} # pragma: no cover
class MockStats(object):# pragma: no cover
    def __init__(self):# pragma: no cover
        self.stats = {'start_time': '2023-10-01T00:00:00Z'} # pragma: no cover
class MockSignals(object):# pragma: no cover
    def connect(self, method, signal): pass # pragma: no cover
signals = MockSignals() # pragma: no cover
class MockCls(object):# pragma: no cover
    def __init__(self, settings, stats):# pragma: no cover
        self.settings = settings# pragma: no cover
        self.stats = stats# pragma: no cover
    def spider_opened(self):# pragma: no cover
        print('Spider opened')# pragma: no cover
    def spider_closed(self):# pragma: no cover
        print('Spider closed') # pragma: no cover
cls = MockCls # pragma: no cover
class MockCrawler(object):# pragma: no cover
    def __init__(self):# pragma: no cover
        self.settings = MockSettings()# pragma: no cover
        self.stats = MockStats()# pragma: no cover
        self.signals = signals # pragma: no cover
crawler = MockCrawler() # pragma: no cover

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
