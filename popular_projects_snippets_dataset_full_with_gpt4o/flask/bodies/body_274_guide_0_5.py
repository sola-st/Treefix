import sys # pragma: no cover

type_envvar = type('MockEnvVar', (object,), {'split_envvar_value': lambda self, value: value.split(',')}) # pragma: no cover
type_super = type('MockSuper', (object,), {'convert': lambda self, item, param, ctx: int(item) * 2}) # pragma: no cover
self = type('Mock', (type_envvar, type_super), {})() # pragma: no cover
value = '1,2,3' # pragma: no cover
param = 'mock_param' # pragma: no cover
ctx = 'mock_ctx' # pragma: no cover

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
