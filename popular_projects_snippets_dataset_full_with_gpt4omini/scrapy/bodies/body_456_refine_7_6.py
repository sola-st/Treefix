from unittest.mock import Mock # pragma: no cover

self = Mock() # pragma: no cover
self.site = Mock() # pragma: no cover

from unittest import TestCase # pragma: no cover
from unittest.mock import Mock # pragma: no cover

class MockTest(TestCase):# pragma: no cover
    def tearDown(self):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
self = MockTest() # pragma: no cover
self.site = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(9220)
self.site.stopListening()
_l_(9221)
