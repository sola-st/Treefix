self = type('MockSelf', (object,), {})() # pragma: no cover
self.site = type('MockSite', (object,), {'stopListening': lambda: None})() # pragma: no cover

import unittest # pragma: no cover

class MockSite:# pragma: no cover
    def stopListening(self):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
class MockSelf(unittest.TestCase):# pragma: no cover
    def setUp(self):# pragma: no cover
        self.site = MockSite()# pragma: no cover
# pragma: no cover
    def tearDown(self):# pragma: no cover
        super().tearDown()# pragma: no cover
# pragma: no cover
self = MockSelf()# pragma: no cover
self.setUp() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(20352)
self.site.stopListening()
_l_(20353)
