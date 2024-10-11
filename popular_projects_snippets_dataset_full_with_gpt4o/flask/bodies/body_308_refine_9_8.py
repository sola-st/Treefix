from functools import update_wrapper # pragma: no cover
from typing import Any, cast # pragma: no cover

f = lambda self, *args, **kwargs: print('function f called') # pragma: no cover
t = type('Mock', (object,), { 'Any': Any, 'cast': cast }) # pragma: no cover
F = type('MockF', (object,), {}) # pragma: no cover

from functools import update_wrapper # pragma: no cover
from typing import Any, cast # pragma: no cover

class MockClass: # pragma: no cover
    def _check_setup_finished(self, name): # pragma: no cover
        print(f"Checking setup finished for {name}") # pragma: no cover
    def mock_function(self, *args, **kwargs): # pragma: no cover
        print('Executing mock function') # pragma: no cover
f = MockClass().mock_function # pragma: no cover
t = type('Mock', (object,), {'Any': Any, 'cast': cast}) # pragma: no cover
F = type('MockF', (object,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
f_name = f.__name__
_l_(22490)

def wrapper_func(self, *args: t.Any, **kwargs: t.Any) -> t.Any:
    _l_(22493)

    self._check_setup_finished(f_name)
    _l_(22491)
    aux = f(self, *args, **kwargs)
    _l_(22492)
    exit(aux)
aux = t.cast(F, update_wrapper(wrapper_func, f))
_l_(22494)

exit(aux)
