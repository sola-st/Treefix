from typing import Callable # pragma: no cover

class Mock: pass # pragma: no cover
initial = None # pragma: no cover
def on_update_method(): pass # pragma: no cover
setattr(Mock, 'on_update', on_update_method) # pragma: no cover
mock_instance = Mock() # pragma: no cover
mock_instance.initial = initial # pragma: no cover
mock_instance.on_update = mock_instance.on_update # pragma: no cover

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
