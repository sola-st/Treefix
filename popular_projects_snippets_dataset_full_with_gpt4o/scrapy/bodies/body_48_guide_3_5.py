from typing import Any, Dict # pragma: no cover

class Base: # pragma: no cover
    def __init__(self, *args: Any, **kwargs: Dict[str, Any]) -> None: # pragma: no cover
        print('Base __init__ executed with args:', args, 'and kwargs:', kwargs) # pragma: no cover
 # pragma: no cover
a = () # pragma: no cover
kw = {'print_help': True} # pragma: no cover
self = type('MockClass', (Base,), {})() # pragma: no cover
self.__class__.__bases__ = (Base,) # pragma: no cover
Base.__init__(self, *a, **kw) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exceptions.py
from l3.Runtime import _l_
self.print_help = kw.pop('print_help', True)
_l_(21639)
super().__init__(*a, **kw)
_l_(21640)
