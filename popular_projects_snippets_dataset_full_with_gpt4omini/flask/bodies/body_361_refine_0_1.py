from typing import Any # pragma: no cover

initial = {'key': 'value'} # pragma: no cover

from typing import Any # pragma: no cover

class MockBase: pass # pragma: no cover
initial = {} # pragma: no cover
on_update = lambda self: (setattr(self, 'modified', True), setattr(self, 'accessed', True))[-1] # pragma: no cover
self = type('Mock', (MockBase,), {})() # pragma: no cover
setattr(self, 'modified', False) # pragma: no cover
setattr(self, 'accessed', False) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
def on_update(self) -> None:
    _l_(6317)

    self.modified = True
    _l_(6315)
    self.accessed = True
    _l_(6316)

super().__init__(initial, on_update)
_l_(6318)
