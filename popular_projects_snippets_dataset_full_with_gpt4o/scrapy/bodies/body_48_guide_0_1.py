import sys # pragma: no cover

a = () # pragma: no cover
kw = {'print_help': False} # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
def __init__(self, *a, **kw): pass # pragma: no cover
self.__class__ = type('Mock', (object,), {'__init__': __init__}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exceptions.py
from l3.Runtime import _l_
self.print_help = kw.pop('print_help', True)
_l_(21639)
super().__init__(*a, **kw)
_l_(21640)
