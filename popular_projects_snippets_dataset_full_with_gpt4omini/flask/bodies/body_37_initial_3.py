from functools import update_wrapper # pragma: no cover

class BlueprintSetupState:# pragma: no cover
    def __init__(self, first_registration: bool):# pragma: no cover
        self.first_registration = first_registration # pragma: no cover
self = type('Mock', (object,), {'record': lambda x: None})() # pragma: no cover
func = lambda state: print('Function called') # pragma: no cover
wrapper = None  # Initialize wrapper later in the code snippet as it references func # pragma: no cover

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
