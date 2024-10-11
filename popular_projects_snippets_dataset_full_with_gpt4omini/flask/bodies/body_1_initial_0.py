from types import SimpleNamespace # pragma: no cover

self = SimpleNamespace() # pragma: no cover
name = 'example_name' # pragma: no cover
value = 42 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
self.__dict__[name] = value
_l_(8533)
