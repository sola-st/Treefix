from collections import defaultdict # pragma: no cover

class MockBase(object): # pragma: no cover
    def get(self, key, def_val): # pragma: no cover
        return [] # pragma: no cover
   # pragma: no cover
   # pragma: no cover
key = 'test_key' # pragma: no cover
def_val = 'default_value' # pragma: no cover
mock_instance = MockBase() # pragma: no cover
super = lambda: mock_instance # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/http/headers.py
from l3.Runtime import _l_
try:
    _l_(6763)

    aux = super().get(key, def_val)[-1]
    _l_(6760)
    exit(aux)
except IndexError:
    _l_(6762)

    aux = None
    _l_(6761)
    exit(aux)
