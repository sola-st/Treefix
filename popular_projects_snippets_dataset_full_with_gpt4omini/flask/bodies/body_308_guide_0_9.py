from functools import update_wrapper # pragma: no cover
from typing import Any, cast, Callable, TypeVar # pragma: no cover

F = TypeVar('F', bound=Callable) # pragma: no cover
class Mock:  # Define a mock class for self that contains the required method # pragma: no cover
    def _check_setup_finished(self, f_name): pass # pragma: no cover
f = lambda self, *args, **kwargs: 'function executed' # pragma: no cover
# Define a mock function f that mimics the expected function signature # pragma: no cover

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
