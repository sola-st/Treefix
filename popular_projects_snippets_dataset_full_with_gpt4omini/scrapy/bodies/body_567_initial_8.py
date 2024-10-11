from collections import UserDict # pragma: no cover

key = 'example_key' # pragma: no cover
class Mock(UserDict): pass # pragma: no cover

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
