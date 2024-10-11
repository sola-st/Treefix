import unittest # pragma: no cover
from unittest.mock import Mock # pragma: no cover

class MyTestCase(unittest.TestCase): # pragma: no cover
    def tearDown(self): # pragma: no cover
        super().tearDown() # pragma: no cover
 # pragma: no cover
self = MyTestCase('tearDown') # pragma: no cover
 # pragma: no cover
MockSite = type('MockSite', (object,), {'stopListening': lambda self: None}) # pragma: no cover
self.site = MockSite() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(20352)
self.site.stopListening()
_l_(20353)
