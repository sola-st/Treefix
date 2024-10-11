initial = 0 # pragma: no cover

class BaseClass:# pragma: no cover
    def __init__(self, initial, on_update):# pragma: no cover
        self.initial = initial# pragma: no cover
        self.on_update = on_update# pragma: no cover
# pragma: no cover
class ChildClass(BaseClass):# pragma: no cover
    def __init__(self, initial, on_update):# pragma: no cover
        super().__init__(initial, on_update)# pragma: no cover
        self.modified = False# pragma: no cover
        self.accessed = False# pragma: no cover
# pragma: no cover
initial = {'key': 'value'}# pragma: no cover
on_update = lambda: None# pragma: no cover
child_instance = ChildClass(initial, on_update) # pragma: no cover

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
