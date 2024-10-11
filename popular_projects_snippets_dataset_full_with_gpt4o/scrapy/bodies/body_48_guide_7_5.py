from typing import Any, Dict # pragma: no cover

class BaseClass: # pragma: no cover
    def __init__(self, *args: Any, **kwargs: Dict[str, Any]) -> None: # pragma: no cover
        print('BaseClass __init__ executed with args:', args, 'and kwargs:', kwargs) # pragma: no cover
 # pragma: no cover
class DerivedClass(BaseClass): # pragma: no cover
    def __init__(self, *a: Any, **kw: Dict[str, Any]) -> None: # pragma: no cover
        self.print_help = kw.pop('print_help', True) # pragma: no cover
        print('Before super() in DerivedClass __init__') # pragma: no cover
        super().__init__(*a, **kw) # uncovered # pragma: no cover
        print('After super() in DerivedClass __init__') # pragma: no cover
kw: Dict[str, Any] = {'print_help': True} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exceptions.py
from l3.Runtime import _l_
self.print_help = kw.pop('print_help', True)
_l_(21639)
super().__init__(*a, **kw)
_l_(21640)
