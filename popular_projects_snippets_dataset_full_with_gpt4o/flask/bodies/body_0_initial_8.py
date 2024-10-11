class Mock(object): # pragma: no cover
    def __init__(self): # pragma: no cover
        self.__dict__ = {'example_attribute': 'example_value'} # pragma: no cover
 # pragma: no cover
self = Mock() # pragma: no cover
name = 'example_attribute' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
try:
    _l_(18913)

    aux = self.__dict__[name]
    _l_(18910)
    exit(aux)
except KeyError:
    _l_(18912)

    raise AttributeError(name) from None
    _l_(18911)
