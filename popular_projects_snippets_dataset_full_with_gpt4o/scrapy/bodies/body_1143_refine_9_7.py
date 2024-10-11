from typing import Any, Dict # pragma: no cover

key = 'some_key' # pragma: no cover
def_val = [1, 2, 3] # pragma: no cover
MockSuper = type('MockSuper', (object,), {'get': lambda self, key, def_val: [1, 2, 3]}) # pragma: no cover
super = lambda: MockSuper() # pragma: no cover

key = 'example_key' # pragma: no cover
def_val = ['default_value'] # pragma: no cover
super_obj = type('SuperObject', (object,), {'get': lambda self, k, d: d}) # pragma: no cover
obj = super_obj() # pragma: no cover
super = lambda: obj # pragma: no cover

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
