from typing import Any, List, Optional # pragma: no cover

value = 'item1,item2,item3' # pragma: no cover
param = None # pragma: no cover
ctx = None # pragma: no cover
class MockSuper:# pragma: no cover
    def convert(self, item: str, param: Optional[Any], ctx: Optional[Any]) -> str:# pragma: no cover
        return f'converted_{item}' # pragma: no cover
Mock = type('Mock', (object,), {'split_envvar_value': lambda self, val: val.split(','), 'convert': MockSuper().convert}) # pragma: no cover
self = Mock() # pragma: no cover

value = 'item1,item2,item3' # pragma: no cover
param = None # pragma: no cover
ctx = None # pragma: no cover
class BaseClass:# pragma: no cover
    def convert(self, item, param, ctx):# pragma: no cover
        return f'converted_{item}' # pragma: no cover
class Mock(BaseClass):# pragma: no cover
    def split_envvar_value(self, value):# pragma: no cover
        return value.split(',') # pragma: no cover
self = Mock() # pragma: no cover

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
