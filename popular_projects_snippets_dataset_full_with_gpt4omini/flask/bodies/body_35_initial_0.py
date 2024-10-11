from typing import Callable # pragma: no cover

self = type('Mock', (object,), {'deferred_functions': []})() # pragma: no cover
func = lambda x: x * 2 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
"""Registers a function that is called when the blueprint is
        registered on the application.  This function is called with the
        state as argument as returned by the :meth:`make_setup_state`
        method.
        """
self.deferred_functions.append(func)
_l_(9314)
