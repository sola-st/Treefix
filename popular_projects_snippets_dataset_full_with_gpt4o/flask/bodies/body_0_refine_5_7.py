self = type('Mock', (object,), {'__dict__': {}})() # pragma: no cover
name = 'attribute_name' # pragma: no cover
self.__dict__[name] = 'attribute_value' # pragma: no cover

name = 'example_attribute' # pragma: no cover
self = type('Mock', (object,), {'__dict__': {'example_attribute': 0}})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
try:
    _l_(18887)

    aux = self.__dict__[name]
    _l_(18884)
    exit(aux)
except KeyError:
    _l_(18886)

    raise AttributeError(name) from None
    _l_(18885)
