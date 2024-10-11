key = 'example_key' # pragma: no cover
def_val = ('default_value',) # pragma: no cover

key = 'example_key' # pragma: no cover
def_val = ['default_value'] # pragma: no cover
class MockSuperClass:# pragma: no cover
    def get(self, key, def_val):# pragma: no cover
        return def_val# pragma: no cover
mock_instance = MockSuperClass() # pragma: no cover

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
