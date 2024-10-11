from typing import Any # pragma: no cover

key = 'example_key' # pragma: no cover
def_val = [1, 2, 3] # pragma: no cover

from collections import MutableMapping # pragma: no cover

class Mock(MutableMapping): # pragma: no cover
    def __init__(self): # pragma: no cover
        self.store = {'example_key': ['value1', 'value2']} # pragma: no cover
    def __getitem__(self, key): # pragma: no cover
        return self.store[key] # pragma: no cover
    def __setitem__(self, key, value): # pragma: no cover
        self.store[key] = value # pragma: no cover
    def __delitem__(self, key): # pragma: no cover
        del self.store[key] # pragma: no cover
    def __iter__(self): # pragma: no cover
        return iter(self.store) # pragma: no cover
    def __len__(self): # pragma: no cover
        return len(self.store) # pragma: no cover
    def get(self, key, def_val): # pragma: no cover
        return self.store.get(key, def_val) # pragma: no cover
mock_data = Mock() # pragma: no cover
key = 'example_key' # pragma: no cover
def_val = ['default_value'] # pragma: no cover

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
