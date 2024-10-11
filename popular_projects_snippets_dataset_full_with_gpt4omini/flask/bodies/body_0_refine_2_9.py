from typing import Any # pragma: no cover

class Mock: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.__dict__ = {'example_name': 42} # pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
name = 'example_name' # pragma: no cover

class Mock: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.__dict__ = {'example': 'value'} # pragma: no cover
self = Mock() # pragma: no cover
name = 'example' # pragma: no cover

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
