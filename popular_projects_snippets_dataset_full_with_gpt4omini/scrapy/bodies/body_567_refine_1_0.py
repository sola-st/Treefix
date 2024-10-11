import weakref # pragma: no cover

import weakref # pragma: no cover

class MockSuper: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.cache = weakref.WeakValueDictionary() # pragma: no cover
    def __getitem__(self, key): # pragma: no cover
        return self.cache[key] # pragma: no cover
 # pragma: no cover
super = MockSuper() # pragma: no cover
key = 'example_key' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/datatypes.py
from l3.Runtime import _l_
try:
    _l_(9166)

    aux = super().__getitem__(key)
    _l_(9163)
    exit(aux)
except (TypeError, KeyError):
    _l_(9165)

    aux = None  # key is either not weak-referenceable or not cached
    _l_(9164)  # key is either not weak-referenceable or not cached
    exit(aux)  # key is either not weak-referenceable or not cached
