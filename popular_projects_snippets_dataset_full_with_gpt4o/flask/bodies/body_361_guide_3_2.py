from typing import Callable # pragma: no cover

initial = 123 # pragma: no cover
class MockBaseClass: # pragma: no cover
    def __init__(self, initial: int, on_update: Callable) -> None: # pragma: no cover
        self.initial = initial # pragma: no cover
        on_update(self) # pragma: no cover
class MockClass(MockBaseClass): # pragma: no cover
    def __init__(self, initial: int) -> None: # pragma: no cover
        self.modified = False # pragma: no cover
        self.accessed = False # pragma: no cover
        def on_update(instance): # pragma: no cover
            instance.modified = True # pragma: no cover
            instance.accessed = True # pragma: no cover
        super().__init__(initial, on_update) # pragma: no cover
self = MockClass(initial) # pragma: no cover

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
