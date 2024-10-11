from functools import update_wrapper # pragma: no cover
from typing import Callable # pragma: no cover

class BlueprintSetupState:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.first_registration = True # pragma: no cover
class Mock:# pragma: no cover
    def record(self, func: Callable):# pragma: no cover
        pass# pragma: no cover
self = Mock() # pragma: no cover
def func(state: BlueprintSetupState) -> None:# pragma: no cover
    pass # pragma: no cover
func = func # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
"""Works like :meth:`record` but wraps the function in another
        function that will ensure the function is only called once.  If the
        blueprint is registered a second time on the application, the
        function passed is not called.
        """

def wrapper(state: BlueprintSetupState) -> None:
    _l_(4987)

    if state.first_registration:
        _l_(4986)

        func(state)
        _l_(4985)

self.record(update_wrapper(wrapper, func))
_l_(4988)
