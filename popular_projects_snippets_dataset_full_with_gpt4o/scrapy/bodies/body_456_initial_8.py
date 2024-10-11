self = type('MockSelf', (object,), {})() # pragma: no cover
self.site = type('MockSite', (object,), {'stopListening': lambda: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(20352)
self.site.stopListening()
_l_(20353)
