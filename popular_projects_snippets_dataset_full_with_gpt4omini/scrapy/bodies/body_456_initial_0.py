from twisted.internet import reactor # pragma: no cover
from twisted.internet.protocol import Protocol, ServerFactory # pragma: no cover

class MockSite:# pragma: no cover
    def stopListening(self):# pragma: no cover
        print('Listening stopped')# pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(9220)
self.site.stopListening()
_l_(9221)
