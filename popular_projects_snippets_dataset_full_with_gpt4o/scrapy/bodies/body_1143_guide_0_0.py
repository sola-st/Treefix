from typing import Any # pragma: no cover

class MockSuper:# pragma: no cover
    def get(self, key: Any, def_val: Any) -> Any:# pragma: no cover
        return def_val # pragma: no cover
key = 'test_key' # pragma: no cover
def_val = [] # pragma: no cover
super = lambda: MockSuper() # pragma: no cover

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
