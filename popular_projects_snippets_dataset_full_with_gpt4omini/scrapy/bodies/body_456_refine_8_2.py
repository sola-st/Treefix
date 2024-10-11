from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover
from twisted.internet.protocol import ServerFactory # pragma: no cover

from unittest import TestCase # pragma: no cover

class MockSite:# pragma: no cover
    def stopListening(self):# pragma: no cover
        print('Site stopped listening') # pragma: no cover
class TestClass(TestCase):# pragma: no cover
    def setUp(self):# pragma: no cover
        self.site = MockSite()# pragma: no cover
# pragma: no cover
    def tearDown(self):# pragma: no cover
        super().tearDown()  # Call to superclass tearDown# pragma: no cover
# pragma: no cover
self = TestClass()  # Create an instance of the test class # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(9220)
self.site.stopListening()
_l_(9221)
