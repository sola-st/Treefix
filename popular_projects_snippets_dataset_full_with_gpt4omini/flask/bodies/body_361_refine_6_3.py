from typing import Any # pragma: no cover

initial = { 'key': 'value' } # pragma: no cover
self = type('Mock', (object,), {'modified': False, 'accessed': False})() # pragma: no cover

class Mock:  # Create a mock class to simulate the superclass # pragma: no cover
    def __init__(self, initial, on_update): # pragma: no cover
        self.initial = initial # pragma: no cover
        self.on_update = on_update # pragma: no cover
        self.modified = False # pragma: no cover
        self.accessed = False # pragma: no cover
 # pragma: no cover
initial = {'key': 'value'} # pragma: no cover
on_update = lambda: None # pragma: no cover
self = Mock(initial, on_update) # pragma: no cover

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
