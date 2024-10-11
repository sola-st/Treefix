self = type('MockSelf', (object,), {'print_help': True})() # pragma: no cover
kw = {'print_help': True} # pragma: no cover
a = () # pragma: no cover

class MockParent:# pragma: no cover
    def __init__(self, *a, **kw):# pragma: no cover
        pass # pragma: no cover
a = (1, 2) # pragma: no cover
kw = {'print_help': False} # pragma: no cover
self = type('MockSelf', (MockParent,), {'print_help': True})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exceptions.py
from l3.Runtime import _l_
self.print_help = kw.pop('print_help', True)
_l_(21639)
super().__init__(*a, **kw)
_l_(21640)
