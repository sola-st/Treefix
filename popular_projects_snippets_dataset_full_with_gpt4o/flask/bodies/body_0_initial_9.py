class Mock(object):# pragma: no cover
    def __init__(self, **kwargs):# pragma: no cover
        self.__dict__.update(kwargs) # pragma: no cover
self = Mock(name='test_attribute') # pragma: no cover
name = 'name' # pragma: no cover

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
