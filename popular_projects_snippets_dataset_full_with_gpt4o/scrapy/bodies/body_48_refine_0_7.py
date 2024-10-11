self = type('MockSelf', (object,), {'print_help': True})() # pragma: no cover
kw = {'some_key': 'some_value', 'print_help': True} # pragma: no cover
a = ['arg1', 'arg2'] # pragma: no cover

class BaseClass: # pragma: no cover
    def __init__(self, *args, **kwargs): # pragma: no cover
        pass # pragma: no cover
class MockSelf(BaseClass): # pragma: no cover
    def __init__(self, *args, **kwargs): # pragma: no cover
        self.print_help = kwargs.pop('print_help', True) # pragma: no cover
        super().__init__(*args, **kwargs) # pragma: no cover
self = MockSelf() # pragma: no cover
kw = {'some_key': 'some_value', 'print_help': True} # pragma: no cover
a = ['arg1', 'arg2'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exceptions.py
from l3.Runtime import _l_
self.print_help = kw.pop('print_help', True)
_l_(21639)
super().__init__(*a, **kw)
_l_(21640)
