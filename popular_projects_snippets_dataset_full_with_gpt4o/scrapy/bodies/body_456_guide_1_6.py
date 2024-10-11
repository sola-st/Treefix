import unittest # pragma: no cover
from unittest.mock import Mock # pragma: no cover

class BaseTestCase(unittest.TestCase):# pragma: no cover
    def tearDown(self):# pragma: no cover
        super().tearDown() # pragma: no cover
self = type('TestMock', (BaseTestCase,), {})() # pragma: no cover
self.site = type('SiteMock', (object,), {'stopListening': Mock()})() # pragma: no cover
self.site.stopListening.return_value = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(20352)
self.site.stopListening()
_l_(20353)
