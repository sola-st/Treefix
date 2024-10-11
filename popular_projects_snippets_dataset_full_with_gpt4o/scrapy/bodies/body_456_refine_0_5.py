import unittest # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

self = type('Mock', (unittest.TestCase,), {'tearDown': MagicMock()})() # pragma: no cover
self.site = MagicMock(stopListening=MagicMock()) # pragma: no cover

import unittest # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

class MockTestCase(unittest.TestCase):# pragma: no cover
    def tearDown(self):# pragma: no cover
        super().tearDown()# pragma: no cover
self = MockTestCase() # pragma: no cover
self.site = MagicMock(stopListening=MagicMock()) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(20352)
self.site.stopListening()
_l_(20353)
