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
