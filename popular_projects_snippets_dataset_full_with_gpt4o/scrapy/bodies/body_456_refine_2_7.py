self = type('MockSelf', (object,), {'site': type('MockSite', (object,), {'stopListening': lambda self: None})()})() # pragma: no cover

import unittest # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

class MockSelf(unittest.TestCase): # pragma: no cover
    def __init__(self, *args, **kwargs): # pragma: no cover
        super().__init__(*args, **kwargs) # pragma: no cover
        self.site = type('MockSite', (object,), {'stopListening': MagicMock()})() # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
from l3.Runtime import _l_
super().tearDown()
_l_(20352)
self.site.stopListening()
_l_(20353)
