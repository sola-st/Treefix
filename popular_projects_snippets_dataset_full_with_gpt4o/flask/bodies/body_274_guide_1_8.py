import sys # pragma: no cover

class MockBase: # pragma: no cover
    def convert(self, value, param, ctx): # pragma: no cover
        return value.upper() # pragma: no cover
 # pragma: no cover
class Mock(MockBase): # pragma: no cover
    def split_envvar_value(self, value): # pragma: no cover
        return value.split(',') # pragma: no cover
 # pragma: no cover
self = Mock() # pragma: no cover
value = 'a,b,c' # pragma: no cover
param = None # pragma: no cover
ctx = None # pragma: no cover

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
