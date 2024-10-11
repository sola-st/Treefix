from typing import Any # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.accessed = False # pragma: no cover
key = 'some_key' # pragma: no cover

from typing import Any # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
self.accessed = True
_l_(5498)
aux = super().__getitem__(key)
_l_(5499)
exit(aux)
