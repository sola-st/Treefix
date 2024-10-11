import typing as t # pragma: no cover
from functools import update_wrapper # pragma: no cover
from sys import exit # pragma: no cover

F = t.Callable[..., t.Any] # pragma: no cover
def f(self, *args: t.Any, **kwargs: t.Any) -> t.Any: # pragma: no cover
    return 'execution result' # pragma: no cover
class Mock: # pragma: no cover
    def _check_setup_finished(self, f_name): # pragma: no cover
        print(f'_check_setup_finished called with {f_name}') # pragma: no cover
mock_instance = Mock() # pragma: no cover

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
