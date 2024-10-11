from twisted.internet import protocol # pragma: no cover
from twisted.internet import reactor # pragma: no cover

class MockSite:  # A mock site class to replicate expected behavior# pragma: no cover
    def stopListening(self):# pragma: no cover
        pass # pragma: no cover
self = type('Mock', (object,), {'site': MockSite()})() # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import Protocol, ServerFactory # pragma: no cover
from twisted.trial import unittest # pragma: no cover

class MockSite:# pragma: no cover
    def stopListening(self):# pragma: no cover
        pass # pragma: no cover
class MockTestCase(unittest.TestCase):# pragma: no cover
    def tearDown(self):# pragma: no cover
        pass# pragma: no cover
self = MockTestCase() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(9220)
self.site.stopListening()
_l_(9221)
