from typing import List # pragma: no cover
from click import Parameter, Context # pragma: no cover

class MockConverter: # pragma: no cover
    def split_envvar_value(self, value: str) -> List[str]: # pragma: no cover
        return value.split(',') # pragma: no cover
 # pragma: no cover
    def convert(self, item: str, param: Parameter, ctx: Context): # pragma: no cover
        return item.strip() # pragma: no cover
 # pragma: no cover
mock_instance = type( # pragma: no cover
    'Mock', # pragma: no cover
    (MockConverter,), # pragma: no cover
    { # pragma: no cover
        'convert': MockConverter().convert, # pragma: no cover
    } # pragma: no cover
)() # pragma: no cover
 # pragma: no cover
value = 'item1, item2, item3' # pragma: no cover

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
