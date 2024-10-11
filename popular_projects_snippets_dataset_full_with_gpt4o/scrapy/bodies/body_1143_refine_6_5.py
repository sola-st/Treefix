key = 'example_key' # pragma: no cover
def_val = ['default_value'] # pragma: no cover
super_mock = type('MockSuper', (object,), {'get': lambda self, k, dv: dv}) # pragma: no cover
super = super_mock() # pragma: no cover

key = 'example_key' # pragma: no cover
def_val = ['default_value'] # pragma: no cover

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
