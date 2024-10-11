import click # pragma: no cover

self = type('Mock', (object,), {'split_envvar_value': lambda self, x: x.split(',')})() # pragma: no cover
param = None # pragma: no cover
ctx = None # pragma: no cover
super = lambda: type('MockSuper', (object,), {'convert': lambda self, item, param, ctx: item}) # pragma: no cover

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
