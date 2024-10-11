from collections import defaultdict # pragma: no cover

self = type('Mock', (object,), {'print_help': True})() # pragma: no cover
kw = defaultdict(lambda: True) # pragma: no cover
a = () # pragma: no cover

from types import SimpleNamespace # pragma: no cover

class Base: pass # pragma: no cover
self = SimpleNamespace() # pragma: no cover
self.print_help = True # pragma: no cover
kw = {'print_help': True} # pragma: no cover
a = () # pragma: no cover
Base.__init__ = lambda self, *args, **kwargs: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exceptions.py
from l3.Runtime import _l_
self.print_help = kw.pop('print_help', True)
_l_(10279)
super().__init__(*a, **kw)
_l_(10280)
