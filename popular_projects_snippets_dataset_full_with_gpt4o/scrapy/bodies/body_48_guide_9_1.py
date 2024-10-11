from typing import Any, Dict # pragma: no cover

class BaseClass: # pragma: no cover
    def __init__(self, *args: Any, **kwargs: Dict[str, Any]) -> None: # pragma: no cover
        print('BaseClass __init__ executed with args:', args, 'and kwargs:', kwargs) # pragma: no cover
 # pragma: no cover
class MockClass(BaseClass): # pragma: no cover
    def __init__(self, *a: Any, **kw: Dict[str, Any]) -> None: # pragma: no cover
        self.print_help = kw.pop('print_help', True) # pragma: no cover
        print('MockClass __init__ before super()') # pragma: no cover
        super().__init__(*a, **kw) # uncovered # pragma: no cover
        print('MockClass __init__ after super()') # pragma: no cover
 # pragma: no cover
a = (1,) # pragma: no cover
kw = {'print_help': True} # pragma: no cover
self = MockClass(*a, **kw) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exceptions.py
from l3.Runtime import _l_
self.print_help = kw.pop('print_help', True)
_l_(21639)
super().__init__(*a, **kw)
_l_(21640)
