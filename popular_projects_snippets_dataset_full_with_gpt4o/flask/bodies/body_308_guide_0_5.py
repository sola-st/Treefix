import typing as t # pragma: no cover
from functools import update_wrapper # pragma: no cover
from typing import Callable, TypeVar # pragma: no cover

F = TypeVar('F', bound=Callable) # pragma: no cover
def mock_func(self, *args, **kwargs): return 'mock' # pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self._setup_finished = True# pragma: no cover
    def _check_setup_finished(self, f_name):# pragma: no cover
        if not self._setup_finished:# pragma: no cover
            raise RuntimeError('Setup not finished')# pragma: no cover
    def test_method(self):# pragma: no cover
        return 'test executed' # pragma: no cover
f = Mock.test_method # pragma: no cover
self = Mock() # pragma: no cover

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
