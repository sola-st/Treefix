from typing import Any # pragma: no cover

class Mock(object): # pragma: no cover
    def split_envvar_value(self, value: str): # pragma: no cover
        return value.split(':') # pragma: no cover
 # pragma: no cover
    def convert(self, item: str, param: Any, ctx: Any): # pragma: no cover
        return item.upper() # pragma: no cover
 # pragma: no cover
mock_instance = Mock() # pragma: no cover
self = mock_instance # pragma: no cover
super_convert = mock_instance.convert # pragma: no cover
value = 'a:b:c' # pragma: no cover
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
