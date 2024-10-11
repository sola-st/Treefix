from typing import Any, Dict, Tuple # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.print_help = True # pragma: no cover
kw = {'print_help': False} # pragma: no cover
a = (1, 2, 3) # pragma: no cover

from typing import Any, Dict # pragma: no cover

class MockBase: pass # pragma: no cover
class Mock(MockBase):# pragma: no cover
    def __init__(self, *args, **kwargs): pass # pragma: no cover
self = Mock() # pragma: no cover
self.print_help = True # pragma: no cover
kw = {'print_help': False} # pragma: no cover
a = () # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exceptions.py
from l3.Runtime import _l_
self.print_help = kw.pop('print_help', True)
_l_(10279)
super().__init__(*a, **kw)
_l_(10280)
