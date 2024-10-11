from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover
from twisted.internet.endpoints import TCP4ServerEndpoint # pragma: no cover
from twisted.application import service, internet # pragma: no cover

from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import Protocol # pragma: no cover
from twisted.application import service, internet # pragma: no cover

class MockBaseTestCase:# pragma: no cover
    def tearDown(self):# pragma: no cover
        print('Base tearDown called')# pragma: no cover
# pragma: no cover
class MockSite:# pragma: no cover
    def stopListening(self):# pragma: no cover
        print('Listening stopped')# pragma: no cover
# pragma: no cover
self = type('MockTest', (MockBaseTestCase,), {})()# pragma: no cover
self.site = MockSite() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(9220)
self.site.stopListening()
_l_(9221)
