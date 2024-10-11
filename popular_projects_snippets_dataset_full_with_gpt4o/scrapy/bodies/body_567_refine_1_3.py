key = 'example_key' # pragma: no cover

class BaseClass:# pragma: no cover
    def __getitem__(self, key):# pragma: no cover
        return 'value_from_base' # pragma: no cover
class DerivedClass(BaseClass):# pragma: no cover
    def __getitem__(self, key):# pragma: no cover
        return super().__getitem__(key) # pragma: no cover
key = 'example_key' # pragma: no cover
obj = DerivedClass() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/datatypes.py
from l3.Runtime import _l_
try:
    _l_(20273)

    aux = super().__getitem__(key)
    _l_(20270)
    exit(aux)
except (TypeError, KeyError):
    _l_(20272)

    aux = None  # key is either not weak-referenceable or not cached
    _l_(20271)  # key is either not weak-referenceable or not cached
    exit(aux)  # key is either not weak-referenceable or not cached
