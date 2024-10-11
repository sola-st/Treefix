import unittest # pragma: no cover

self = type('Mock', (object,), {'site': type('Mock', (object,), {'stopListening': lambda: None})()})() # pragma: no cover

import unittest # pragma: no cover

class MockSite:# pragma: no cover
    def stopListening(self):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
class MockTestCase(unittest.TestCase):# pragma: no cover
    def setUp(self):# pragma: no cover
        self.site = MockSite()# pragma: no cover
    def tearDown(self):# pragma: no cover
        # Overriding tearDown to avoid calling super().tearDown()# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
# Create an instance of the test case and set up the required attributes# pragma: no cover
self = MockTestCase()# pragma: no cover
self.setUp() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(20352)
self.site.stopListening()
_l_(20353)
