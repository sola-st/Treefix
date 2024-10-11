import unittest # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

class SiteMock(MagicMock): # pragma: no cover
    def stopListening(self): # pragma: no cover
        print('stopListening called') # pragma: no cover
 # pragma: no cover
class MyTestClass(unittest.TestCase): # pragma: no cover
    def setUp(self): # pragma: no cover
        self.site = SiteMock() # pragma: no cover
 # pragma: no cover
    def test_method(self): # pragma: no cover
        super(MyTestClass, self).tearDown() # pragma: no cover
        self.site.stopListening() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(20352)
self.site.stopListening()
_l_(20353)
