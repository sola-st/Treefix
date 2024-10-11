from typing import Any # pragma: no cover

value = 'item1,item2,item3' # pragma: no cover
param = None # pragma: no cover
ctx = None # pragma: no cover
self = type('Mock', (object,), {'split_envvar_value': lambda self, v: v.split(',')})() # pragma: no cover

from typing import Any # pragma: no cover

value = 'item1,item2,item3' # pragma: no cover
param = None # pragma: no cover
ctx = None # pragma: no cover
class BaseConverter:# pragma: no cover
    def convert(self, item: Any, param: Any, ctx: Any) -> Any:# pragma: no cover
        return f'converted_{item}' # pragma: no cover
class Mock(BaseConverter):# pragma: no cover
    pass
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
