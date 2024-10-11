from types import SimpleNamespace # pragma: no cover

self = SimpleNamespace() # pragma: no cover
name = 'some_attribute' # pragma: no cover
self.__dict__['some_attribute'] = 'some_value' # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.__dict__ = {'name': 'value'} # pragma: no cover
name = 'name' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
try:
    _l_(7711)

    aux = self.__dict__[name]
    _l_(7708)
    exit(aux)
except KeyError:
    _l_(7710)

    raise AttributeError(name) from None
    _l_(7709)
