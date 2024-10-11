from unittest.mock import Mock # pragma: no cover

self = Mock() # pragma: no cover
spider = Mock() # pragma: no cover
self.stats = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/corestats.py
from l3.Runtime import _l_
self.stats.inc_value('response_received_count', spider=spider)
_l_(6133)
