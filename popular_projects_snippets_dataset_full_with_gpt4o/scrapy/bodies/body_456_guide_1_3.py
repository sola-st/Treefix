import unittest # pragma: no cover
from unittest.mock import Mock # pragma: no cover

class MockBaseTestCase(unittest.TestCase): # pragma: no cover
    def tearDown(self): # pragma: no cover
        pass # pragma: no cover
self = type('MockTest', (MockBaseTestCase,), {})() # pragma: no cover
self.site = type('MockSite', (object,), {'stopListening': lambda self: print('stopListening() called')})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(20352)
self.site.stopListening()
_l_(20353)
