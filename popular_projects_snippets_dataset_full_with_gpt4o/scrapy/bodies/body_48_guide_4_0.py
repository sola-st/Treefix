from typing import Any # pragma: no cover

a = () # pragma: no cover
kw = {'print_help': True} # pragma: no cover
class BaseClass: # pragma: no cover
    def __init__(self, *a: Any, **kw: Any) -> None: # pragma: no cover
        print('BaseClass __init__ executed') # pragma: no cover
 # pragma: no cover
class DerivedClass(BaseClass): # pragma: no cover
    def __init__(self, *a: Any, **kw: Any) -> None: # pragma: no cover
        self.print_help = kw.pop('print_help', True) # pragma: no cover
        super().__init__(*a, **kw) # pragma: no cover
 # pragma: no cover
self = DerivedClass(*a, **kw) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exceptions.py
from l3.Runtime import _l_
self.print_help = kw.pop('print_help', True)
_l_(21639)
super().__init__(*a, **kw)
_l_(21640)
