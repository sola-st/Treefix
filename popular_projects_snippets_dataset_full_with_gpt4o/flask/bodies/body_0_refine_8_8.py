class MockClass: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.__dict__ = {'example_name': 'example_value'} # pragma: no cover
self = MockClass() # pragma: no cover
name = 'example_name' # pragma: no cover

class MockClass: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.__dict__ = {'example_name': 0} # pragma: no cover
self = MockClass() # pragma: no cover
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
