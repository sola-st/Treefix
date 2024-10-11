from typing import Any, cast # pragma: no cover
from functools import update_wrapper # pragma: no cover

class Mock: # pragma: no cover
    def _check_setup_finished(self, name): pass # pragma: no cover
f = Mock() # pragma: no cover
t = type('MockT', (object,), {'Any': Any, 'cast': cast})() # pragma: no cover
F = type('MockF', (object,), {}) # pragma: no cover

from typing import Any, cast # pragma: no cover
from functools import update_wrapper # pragma: no cover

class Mock: # pragma: no cover
    def _check_setup_finished(self, name): pass # pragma: no cover
    def __call__(self, *args, **kwargs): return 'called'# pragma: no cover
 # pragma: no cover
f = Mock() # pragma: no cover
f.__name__ = 'mock_function' # pragma: no cover
t = type('MockT', (object,), {'Any': Any, 'cast': cast})() # pragma: no cover
F = type('MockF', (object,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
f_name = f.__name__
_l_(4186)

def wrapper_func(self, *args: t.Any, **kwargs: t.Any) -> t.Any:
    _l_(4189)

    self._check_setup_finished(f_name)
    _l_(4187)
    aux = f(self, *args, **kwargs)
    _l_(4188)
    exit(aux)
aux = t.cast(F, update_wrapper(wrapper_func, f))
_l_(4190)

exit(aux)
