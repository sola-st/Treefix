name = 'attribute_name' # pragma: no cover
self = type('Mock', (object,), {'__dict__': {'attribute_name': 42}})() # pragma: no cover

class Mock: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.__dict__ = {'example_name': sys.exit} # pragma: no cover
self = Mock() # pragma: no cover
name = 'example_name' # pragma: no cover

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
