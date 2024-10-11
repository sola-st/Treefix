from typing import Any # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.__class__.__name__ = 'Mock' # pragma: no cover
self.__dict__ = {'key1': 'value1', 'key2': 'value2'} # pragma: no cover

from types import SimpleNamespace # pragma: no cover

self = SimpleNamespace() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/config.py
from l3.Runtime import _l_
aux = f"<{type(self).__name__} {dict.__repr__(self)}>"
_l_(5543)
exit(aux)
