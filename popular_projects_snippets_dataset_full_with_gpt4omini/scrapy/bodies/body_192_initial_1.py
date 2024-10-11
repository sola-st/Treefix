import scrapy # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self.crawler = type('MockCrawler', (object,), {'settings': type('MockSettings', (object,), {'getfloat': lambda self, key: 10.0})()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/throttle.py
from l3.Runtime import _l_
aux = self.crawler.settings.getfloat('AUTOTHROTTLE_MAX_DELAY')
_l_(8641)
exit(aux)
