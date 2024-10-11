import unittest # pragma: no cover

class SiteMock: # pragma: no cover
    def stopListening(self): # pragma: no cover
        print('stopListening called') # pragma: no cover
 # pragma: no cover
class BaseTestCase(unittest.TestCase): # pragma: no cover
    def tearDown(self): # pragma: no cover
        print('super().tearDown() called') # pragma: no cover
 # pragma: no cover
self = type('TestCase', (BaseTestCase,), {})() # pragma: no cover
self.site = SiteMock() # pragma: no cover
self.tearDown() # pragma: no cover
self.site.stopListening() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(20352)
self.site.stopListening()
_l_(20353)
