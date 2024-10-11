from typing import Any, Dict, Tuple # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.print_help = True # pragma: no cover
kw = {'print_help': False} # pragma: no cover
a = () # pragma: no cover

from typing import Any # pragma: no cover

class BaseClass: pass # pragma: no cover
class Mock(BaseClass):# pragma: no cover
    def __init__(self, *args: Any, **kwargs: Any):# pragma: no cover
        super().__init__() # pragma: no cover
self = Mock() # pragma: no cover
kw = {'print_help': True} # pragma: no cover
a = () # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exceptions.py
from l3.Runtime import _l_
self.print_help = kw.pop('print_help', True)
_l_(10279)
super().__init__(*a, **kw)
_l_(10280)
