import unittest # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

self = type('MockTestCase', (unittest.TestCase,), {'site': MagicMock()})() # pragma: no cover
self.site.stopListening = MagicMock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(9220)
self.site.stopListening()
_l_(9221)
