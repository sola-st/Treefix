from typing import List, Any # pragma: no cover

class Mock: # pragma: no cover
    def split_envvar_value(self, value: str) -> List[str]: # pragma: no cover
        return value.split(',') # pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
value = 'item1,item2,item3' # pragma: no cover
param = 'example_param' # pragma: no cover
ctx = {'key': 'example_context'} # pragma: no cover

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
