import unittest # pragma: no cover

class MockSite: # pragma: no cover
    def stopListening(self): # pragma: no cover
        print('stopListening called') # pragma: no cover
 # pragma: no cover
class MockBase(unittest.TestCase): # pragma: no cover
    def tearDown(self): # pragma: no cover
        print('Base tearDown called') # pragma: no cover
 # pragma: no cover
mock_instance = type('DerivedClass', (MockBase,), {})() # pragma: no cover
mock_instance.site = MockSite() # pragma: no cover
super(type(mock_instance), mock_instance).tearDown() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(20352)
self.site.stopListening()
_l_(20353)
