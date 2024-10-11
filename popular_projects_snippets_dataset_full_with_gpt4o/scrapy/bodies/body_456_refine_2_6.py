self = type('MockSelf', (object,), {'site': type('MockSite', (object,), {'stopListening': lambda self: None})()})() # pragma: no cover

import unittest # pragma: no cover

class MockTest(unittest.TestCase):# pragma: no cover
    def setUp(self):# pragma: no cover
        pass
self = MockTest(methodName='setUp')# pragma: no cover
self.setUp() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(20352)
self.site.stopListening()
_l_(20353)
