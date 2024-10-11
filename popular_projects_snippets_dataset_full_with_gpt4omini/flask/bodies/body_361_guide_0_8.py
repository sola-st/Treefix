from typing import Callable # pragma: no cover

class MockBase(object): # pragma: no cover
    def __init__(self, initial, on_update: Callable): # pragma: no cover
        self.initial = initial # pragma: no cover
        self.on_update = on_update # pragma: no cover
        self.modified = False # pragma: no cover
        self.accessed = False # pragma: no cover
 # pragma: no cover
initial = 'some initial value' # pragma: no cover
on_update = lambda: None # pragma: no cover
Mock = type('Mock', (MockBase,), {}) # pragma: no cover
instance = Mock(initial, on_update) # pragma: no cover

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
