from types import FunctionType # pragma: no cover
from typing import Any, cast # pragma: no cover
from functools import wraps # pragma: no cover

f = type('Mock', (object,), {'__name__': 'mock_function'})() # pragma: no cover
t = type('Mock', (object,), {'Any': Any, 'cast': cast}) # pragma: no cover
F = FunctionType # pragma: no cover
update_wrapper = wraps # pragma: no cover

from typing import Any, Callable, TypeVar, cast # pragma: no cover
from functools import update_wrapper # pragma: no cover

def mock_function(self, *args, **kwargs): return 'mock_function_result' # pragma: no cover
f = type('Mock', (object,), {'__name__': 'mock_function', '__call__': mock_function})() # pragma: no cover
t = type('Mock', (object,), {'Any': Any, 'cast': cast}) # pragma: no cover
F = TypeVar('F', bound=Callable) # pragma: no cover
update_wrapper = update_wrapper # pragma: no cover

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
