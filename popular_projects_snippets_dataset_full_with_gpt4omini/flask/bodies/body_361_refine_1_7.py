from typing import Any # pragma: no cover

initial = {'data': 'initial_value'} # pragma: no cover

class BaseMock:  # Mock base class for super() behavior# pragma: no cover
    def __init__(self, initial, on_update):# pragma: no cover
        self.initial = initial# pragma: no cover
        self.on_update = on_update# pragma: no cover
# pragma: no cover
class Mock(BaseMock):# pragma: no cover
    def on_update(self) -> None:# pragma: no cover
        self.modified = True# pragma: no cover
        self.accessed = True# pragma: no cover
# pragma: no cover
initial = {'data': 'initial_value'}# pragma: no cover

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
