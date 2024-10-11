initial = 'example' # pragma: no cover

class BaseClass:# pragma: no cover
    def __init__(self, initial, on_update):# pragma: no cover
        self.initial = initial# pragma: no cover
        on_update(self)# pragma: no cover
# pragma: no cover
initial = 'test_value'# pragma: no cover
class MyClass(BaseClass):# pragma: no cover
    def __init__(self, initial, on_update):# pragma: no cover
        super().__init__(initial, on_update)# pragma: no cover
    def on_update(self):# pragma: no cover
        self.modified = True# pragma: no cover
        self.accessed = True# pragma: no cover
# pragma: no cover
test_instance = MyClass(initial, MyClass.on_update) # pragma: no cover

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
