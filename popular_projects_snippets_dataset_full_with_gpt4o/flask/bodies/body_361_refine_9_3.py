initial = 0 # pragma: no cover

initial = {} # pragma: no cover
BaseClass = type('BaseClass', (object,), {'__init__': lambda self, *args, **kwargs: None}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
def on_update(self) -> None:
    _l_(17781)

    self.modified = True
    _l_(17779)
    self.accessed = True
    _l_(17780)

super().__init__(initial, on_update)
_l_(17782)
