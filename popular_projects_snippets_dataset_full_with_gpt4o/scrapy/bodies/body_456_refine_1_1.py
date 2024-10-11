from unittest import TestCase # pragma: no cover

self = type('MockSelf', (TestCase,), {'site': type('MockSite', (object,), {'stopListening': lambda self: None})()})() # pragma: no cover

from unittest import TestCase # pragma: no cover

class MockSelf(TestCase): # pragma: no cover
    def __init__(self): # pragma: no cover
        super().__init__() # pragma: no cover
        self.site = type('MockSite', (object,), {'stopListening': lambda self: None})() # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(20352)
self.site.stopListening()
_l_(20353)
