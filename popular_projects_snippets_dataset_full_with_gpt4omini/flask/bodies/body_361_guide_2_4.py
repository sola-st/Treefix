class MockBase: pass # pragma: no cover

initial = None # pragma: no cover
def on_update(self): # pragma: no cover
    self.modified = True # pragma: no cover
    self.accessed = True # pragma: no cover
self = type('Mock', (MockBase,), {'modified': False, 'accessed': False, 'on_update': on_update})() # pragma: no cover

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
