class MockBase: # pragma: no cover
    def __init__(self, *args, **kwargs): # pragma: no cover
        print('MockBase __init__ called') # pragma: no cover
 # pragma: no cover
a = (1,) # pragma: no cover
kw = {'print_help': True} # pragma: no cover
MockClass = type('MockClass', (MockBase,), {}) # pragma: no cover
self = MockClass(*a, **kw) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exceptions.py
from l3.Runtime import _l_
self.print_help = kw.pop('print_help', True)
_l_(21639)
super().__init__(*a, **kw)
_l_(21640)
