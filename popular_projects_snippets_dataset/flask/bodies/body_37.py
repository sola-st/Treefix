# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
"""Works like :meth:`record` but wraps the function in another
        function that will ensure the function is only called once.  If the
        blueprint is registered a second time on the application, the
        function passed is not called.
        """

def wrapper(state: BlueprintSetupState) -> None:
    _l_(16618)

    if state.first_registration:
        _l_(16617)

        func(state)
        _l_(16616)

self.record(update_wrapper(wrapper, func))
_l_(16619)
