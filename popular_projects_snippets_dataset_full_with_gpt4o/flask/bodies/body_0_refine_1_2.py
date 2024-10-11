class MockClass:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.__dict__ = {} # pragma: no cover
self = MockClass() # pragma: no cover
name = 'sample_attribute' # pragma: no cover

class MockClass:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.__dict__['sample_attribute'] = 0 # pragma: no cover
self = MockClass() # pragma: no cover
name = 'sample_attribute' # pragma: no cover

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
