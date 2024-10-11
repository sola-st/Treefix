self = type('MockSelf', (object,), {})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/throttle.py
from l3.Runtime import _l_
aux = self.crawler.settings.getfloat('AUTOTHROTTLE_MAX_DELAY')
_l_(8641)
exit(aux)
