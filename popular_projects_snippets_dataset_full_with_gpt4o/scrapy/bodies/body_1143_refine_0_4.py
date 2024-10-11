from typing import Any, Dict # pragma: no cover

key: Any = 'some_key' # pragma: no cover
def_val: Any = [1, 2, 3] # pragma: no cover

from typing import Any, Dict # pragma: no cover
import sys # pragma: no cover

class Mock(dict): # pragma: no cover
    def get(self, key: Any, def_val: Any) -> Any: # pragma: no cover
        return super().get(key, def_val) # pragma: no cover
 # pragma: no cover
key: Any = 'some_key' # pragma: no cover
def_val: Any = [1, 2, 3] # pragma: no cover
 # pragma: no cover
mock = Mock() # pragma: no cover
mock[key] = [10, 20, 30] # pragma: no cover
 # pragma: no cover
class SuperMock: # pragma: no cover
    def get(self, key: Any, def_val: Any) -> Any: # pragma: no cover
        return mock.get(key, def_val) # pragma: no cover
 # pragma: no cover
class UserMock(SuperMock): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
user_instance = UserMock() # pragma: no cover
 # pragma: no cover
sys.modules[__name__] = user_instance # pragma: no cover

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
