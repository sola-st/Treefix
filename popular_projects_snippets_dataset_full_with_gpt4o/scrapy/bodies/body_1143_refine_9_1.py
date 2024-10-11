from typing import Any, Dict # pragma: no cover

key = 'some_key' # pragma: no cover
def_val = [1, 2, 3] # pragma: no cover
MockSuper = type('MockSuper', (object,), {'get': lambda self, key, def_val: [1, 2, 3]}) # pragma: no cover
super = lambda: MockSuper() # pragma: no cover

key = 'sample_key' # pragma: no cover
def_val = [0] # pragma: no cover
super_mock = type('SuperMock', (dict,), {'get': lambda self, key, default: default}) # pragma: no cover
instance = super_mock() # pragma: no cover
super = lambda: instance # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/headers.py
from l3.Runtime import _l_
try:
    _l_(17515)

    aux = super().get(key, def_val)[-1]
    _l_(17512)
    exit(aux)
except IndexError:
    _l_(17514)

    aux = None
    _l_(17513)
    exit(aux)
