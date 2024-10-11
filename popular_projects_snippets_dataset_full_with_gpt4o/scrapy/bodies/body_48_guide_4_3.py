class Base: # pragma: no cover
    def __init__(self, *args, **kwargs): # pragma: no cover
        print('Base __init__ called') # pragma: no cover
 # pragma: no cover
a = (1, 2, 3) # pragma: no cover
kw = {'print_help': True} # pragma: no cover
mock_bases = (Base,) # pragma: no cover
mock_attrs = {'print_help': None} # pragma: no cover
self = type('Mock', mock_bases, mock_attrs)() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exceptions.py
from l3.Runtime import _l_
self.print_help = kw.pop('print_help', True)
_l_(21639)
super().__init__(*a, **kw)
_l_(21640)
