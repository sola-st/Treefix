class Base: # pragma: no cover
    def __init__(self, *args, **kwargs): # pragma: no cover
        print('In Base __init__') # pragma: no cover
 # pragma: no cover
class Mock(Base): # pragma: no cover
    def __init__(self, *a, **kw): # pragma: no cover
        self.print_help = kw.pop('print_help', True) # pragma: no cover
        super().__init__(*a, **kw) # pragma: no cover
 # pragma: no cover
a = (1, 2, 3) # pragma: no cover
kw = {'print_help': True} # pragma: no cover
self = Mock(*a, **kw) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exceptions.py
from l3.Runtime import _l_
self.print_help = kw.pop('print_help', True)
_l_(21639)
super().__init__(*a, **kw)
_l_(21640)
