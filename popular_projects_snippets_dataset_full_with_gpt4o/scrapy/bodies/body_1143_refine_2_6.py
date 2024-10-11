key = 'example_key' # pragma: no cover
def_val = ['default_value'] # pragma: no cover

key = 'example_key' # pragma: no cover
def_val = ['default_value'] # pragma: no cover
class MockBase(dict): # pragma: no cover
    def get(self, key, default=None): # pragma: no cover
        return {'example_key': ['value1', 'value2']} if key == 'example_key' else default # pragma: no cover
self = MockBase() # pragma: no cover

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
