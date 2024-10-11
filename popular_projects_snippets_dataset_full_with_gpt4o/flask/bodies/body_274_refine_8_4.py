from typing import Any # pragma: no cover

value = 'item1,item2,item3' # pragma: no cover
param = None # pragma: no cover
ctx = None # pragma: no cover
self = type('Mock', (object,), {'split_envvar_value': lambda self, v: v.split(',')})() # pragma: no cover

class SuperMock:# pragma: no cover
    def convert(self, item, param, ctx):# pragma: no cover
        return f'converted_{item}' # pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.super = SuperMock()# pragma: no cover
    def split_envvar_value(self, value):# pragma: no cover
        return value.split(',')# pragma: no cover
    def convert(self, item, param, ctx):# pragma: no cover
        return self.super.convert(item, param, ctx) # pragma: no cover
self = Mock() # pragma: no cover
value = 'item1,item2,item3' # pragma: no cover
param = None # pragma: no cover
ctx = None # pragma: no cover
super_convert = self.super.convert # pragma: no cover

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
