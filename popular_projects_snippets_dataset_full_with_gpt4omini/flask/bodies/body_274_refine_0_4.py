from typing import List, Any, Dict # pragma: no cover

class Mock: pass# pragma: no cover
self = Mock() # pragma: no cover
value = 'item1:item2:item3' # pragma: no cover
param = 'param_value' # pragma: no cover
ctx = {'context_key': 'context_value'} # pragma: no cover
self.split_envvar_value = lambda value: value.split(':') # pragma: no cover

from typing import List, Any, Dict # pragma: no cover

class BaseConverter:# pragma: no cover
    def convert(self, item: str, param: str, ctx: Dict[str, Any]) -> str:# pragma: no cover
        return f'Converted({item}, {param}, {ctx})'# pragma: no cover
class Mock(BaseConverter): pass# pragma: no cover
self = Mock() # pragma: no cover
value = 'item1:item2:item3' # pragma: no cover
param = 'param_value' # pragma: no cover
ctx = {'context_key': 'context_value'} # pragma: no cover
self.split_envvar_value = lambda value: value.split(':') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
items = self.split_envvar_value(value)
_l_(5263)
super_convert = super().convert
_l_(5264)
aux = [super_convert(item, param, ctx) for item in items]
_l_(5265)
exit(aux)
