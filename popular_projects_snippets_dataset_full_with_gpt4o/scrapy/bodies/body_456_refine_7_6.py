import unittest.mock as mock # pragma: no cover

self = mock.Mock(spec=['site']) # pragma: no cover
self.site = mock.Mock(spec=['stopListening']) # pragma: no cover

import unittest # pragma: no cover

class MockSite:# pragma: no cover
    def stopListening(self):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
class MockSuper(object):# pragma: no cover
    def tearDown(self):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
self = type('MockSelf', (MockSuper,), {'site': MockSite()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(20352)
self.site.stopListening()
_l_(20353)
