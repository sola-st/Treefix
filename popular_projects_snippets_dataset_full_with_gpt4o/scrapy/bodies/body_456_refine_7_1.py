import unittest.mock as mock # pragma: no cover

self = mock.Mock(spec=['site']) # pragma: no cover
self.site = mock.Mock(spec=['stopListening']) # pragma: no cover

import unittest # pragma: no cover

class MockSuperClass(unittest.TestCase):# pragma: no cover
    def tearDown(self):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
class MockSelf(MockSuperClass):# pragma: no cover
    def __init__(self):# pragma: no cover
        super().__init__()# pragma: no cover
        self.site = type('MockSite', (object,), {'stopListening': lambda self: None})()# pragma: no cover
# pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(20352)
self.site.stopListening()
_l_(20353)
