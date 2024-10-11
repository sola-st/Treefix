import unittest # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

class MockSite: # pragma: no cover
    def stopListening(self): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class TestClass(unittest.TestCase): # pragma: no cover
    def setUp(self): # pragma: no cover
        self.site = MockSite() # pragma: no cover
 # pragma: no cover
    def tearDown(self): # pragma: no cover
        super().tearDown() # pragma: no cover
 # pragma: no cover
test_instance = TestClass() # pragma: no cover
test_instance.setUp() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(20352)
self.site.stopListening()
_l_(20353)
