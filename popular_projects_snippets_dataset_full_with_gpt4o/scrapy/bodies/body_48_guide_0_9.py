from unittest.mock import Mock # pragma: no cover

kw = {'print_help': True} # pragma: no cover
a = [] # pragma: no cover
self = Mock() # pragma: no cover
self.print_help = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exceptions.py
from l3.Runtime import _l_
self.print_help = kw.pop('print_help', True)
_l_(21639)
super().__init__(*a, **kw)
_l_(21640)
