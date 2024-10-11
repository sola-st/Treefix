import unittest # pragma: no cover

class SiteMock:# pragma: no cover
    def stopListening(self):# pragma: no cover
        print('stopListening called') # pragma: no cover
class TestMockBase(unittest.TestCase):# pragma: no cover
    def tearDown(self):# pragma: no cover
        print('tearDown called') # pragma: no cover
self = type('TestMock', (TestMockBase,), {})() # pragma: no cover
self.site = SiteMock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(20352)
self.site.stopListening()
_l_(20353)
