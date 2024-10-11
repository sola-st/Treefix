from unittest.mock import MagicMock # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self.crawler = MagicMock() # pragma: no cover
self.crawler.settings.getfloat = MagicMock(return_value=5.0) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/throttle.py
from l3.Runtime import _l_
aux = self.crawler.settings.getfloat('AUTOTHROTTLE_MAX_DELAY')
_l_(19827)
exit(aux)
