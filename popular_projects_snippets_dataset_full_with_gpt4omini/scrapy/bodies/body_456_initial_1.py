from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover
from twisted.internet import endpoints # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self.site = type('MockSite', (object,), {'stopListening': lambda self: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(9220)
self.site.stopListening()
_l_(9221)
