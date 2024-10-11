from typing import Any, Dict # pragma: no cover

class MockParent:# pragma: no cover
    def __init__(self, *a: Any, **kw: Dict[str, Any]) -> None:# pragma: no cover
        pass # pragma: no cover
kw = {'example_key': 'example_value'} # pragma: no cover
a = (1, 2, 3) # pragma: no cover
self = type('Mock', (MockParent,), {'print_help': True})() # pragma: no cover

class MockParent:# pragma: no cover
    def __init__(self, *a, **kw):# pragma: no cover
        pass # pragma: no cover
kw = {'print_help': True} # pragma: no cover
a = tuple() # pragma: no cover
self = type('Mock', (MockParent,), {})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exceptions.py
from l3.Runtime import _l_
self.print_help = kw.pop('print_help', True)
_l_(21639)
super().__init__(*a, **kw)
_l_(21640)
