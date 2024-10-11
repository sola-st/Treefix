from typing import Any, Dict # pragma: no cover

key = 'example_key' # pragma: no cover
def_val = [1, 2, 3] # pragma: no cover

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
