self = type('MockSelf', (object,), {'__init__': lambda self: None})() # pragma: no cover
kw = {'print_help': True, 'some_other_key': 'some_value'} # pragma: no cover
a = ['arg1', 'arg2'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exceptions.py
from l3.Runtime import _l_
self.print_help = kw.pop('print_help', True)
_l_(21639)
super().__init__(*a, **kw)
_l_(21640)
