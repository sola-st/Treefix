self = type('Mock', (object,), {'print_help': True})() # pragma: no cover
kw = {'print_help': False} # pragma: no cover
a = () # pragma: no cover

class Base: pass # pragma: no cover
class Mock(Base):# pragma: no cover
    def __init__(self, *a, **kw):# pragma: no cover
        self.print_help = kw.get('print_help', True) # pragma: no cover
self = Mock(print_help=False) # pragma: no cover
kw = {'print_help': False} # pragma: no cover
a = () # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exceptions.py
from l3.Runtime import _l_
self.print_help = kw.pop('print_help', True)
_l_(10279)
super().__init__(*a, **kw)
_l_(10280)
