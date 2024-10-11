class MockSpider: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class MockStats:     # pragma: no cover
    def __init__(self):# pragma: no cover
        self.values = {}# pragma: no cover
# pragma: no cover
    def inc_value(self, key, spider=None):# pragma: no cover
        if key in self.values:# pragma: no cover
            self.values[key] += 1# pragma: no cover
        else:# pragma: no cover
            self.values[key] = 1 # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.stats = MockStats() # pragma: no cover

self = MockSelf() # pragma: no cover
spider = MockSpider() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/corestats.py
from l3.Runtime import _l_
self.stats.inc_value('response_received_count', spider=spider)
_l_(17503)
