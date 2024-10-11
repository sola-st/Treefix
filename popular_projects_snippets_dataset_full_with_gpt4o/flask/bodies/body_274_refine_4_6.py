from typing import List # pragma: no cover

self = type('Mock', (object,), {'split_envvar_value': lambda self, x: x.split(',')})() # pragma: no cover
value = 'item1,item2,item3' # pragma: no cover
param = None # pragma: no cover
ctx = None # pragma: no cover

class MockSuper:# pragma: no cover
    def convert(self, item, param, ctx):# pragma: no cover
        return item # pragma: no cover
class MockSelf(MockSuper):# pragma: no cover
    def split_envvar_value(self, value):# pragma: no cover
        return value.split(',') # pragma: no cover
self = MockSelf() # pragma: no cover
value = 'item1,item2,item3' # pragma: no cover
param = 'some_param' # pragma: no cover
ctx = 'some_context' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
items = self.split_envvar_value(value)
_l_(22581)
super_convert = super().convert
_l_(22582)
aux = [super_convert(item, param, ctx) for item in items]
_l_(22583)
exit(aux)
