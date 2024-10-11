class BaseClass: # pragma: no cover
    def __init__(self, *args, **kwargs): # pragma: no cover
        print('BaseClass __init__ executed') # pragma: no cover
 # pragma: no cover
class MockClass(BaseClass): # pragma: no cover
    def __init__(self, *a, **kw): # pragma: no cover
        self.print_help = kw.pop('print_help', True) # pragma: no cover
        super().__init__(*a, **kw) # uncovered # pragma: no cover
        print('MockClass __init__ executed') # pragma: no cover
 # pragma: no cover
a = () # pragma: no cover
kw = {} # pragma: no cover
self = MockClass(*a, **kw) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exceptions.py
from l3.Runtime import _l_
self.print_help = kw.pop('print_help', True)
_l_(21639)
super().__init__(*a, **kw)
_l_(21640)
