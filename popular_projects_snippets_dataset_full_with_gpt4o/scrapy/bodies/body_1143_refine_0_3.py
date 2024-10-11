from typing import Any, Dict # pragma: no cover

key: Any = 'some_key' # pragma: no cover
def_val: Any = [1, 2, 3] # pragma: no cover

from typing import Any, Dict # pragma: no cover

class BaseClass:# pragma: no cover
    def get(self, key: Any, def_val: Any) -> Any:# pragma: no cover
        return {key: def_val}.get(key, def_val) # pragma: no cover
class Mock(BaseClass):# pragma: no cover
    pass # pragma: no cover
key: Any = 'some_key' # pragma: no cover
def_val: Any = [1, 2, 3] # pragma: no cover
mock_instance = Mock() # pragma: no cover

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
