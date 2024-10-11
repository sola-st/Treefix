key = 'example_key' # pragma: no cover
def_val = ('default_value',) # pragma: no cover

import sys # pragma: no cover

key = 'example_key' # pragma: no cover
def_val = ['default_value'] # pragma: no cover
class MockBase:# pragma: no cover
    def get(self, key, default):# pragma: no cover
        return default# pragma: no cover
class DerivedClass(MockBase):# pragma: no cover
    def get(self, key, default):# pragma: no cover
        return super().get(key, default)# pragma: no cover
derived_instance = DerivedClass()# pragma: no cover
def super():# pragma: no cover
    return derived_instance# pragma: no cover
 # pragma: no cover

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
