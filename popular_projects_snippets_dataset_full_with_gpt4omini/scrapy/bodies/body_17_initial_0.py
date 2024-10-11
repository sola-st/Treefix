class Mock(object):# pragma: no cover
    def __init__(self):# pragma: no cover
        self._stats = None # pragma: no cover
stats = {'score': 100, 'level': 5} # pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/statscollectors.py
from l3.Runtime import _l_
self._stats = stats
_l_(4721)
