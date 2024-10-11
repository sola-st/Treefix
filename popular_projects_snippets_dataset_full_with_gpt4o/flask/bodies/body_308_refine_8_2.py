import typing as t # pragma: no cover
from typing import Any # pragma: no cover
from functools import update_wrapper # pragma: no cover

f = type('Mock', (object,), {'__name__': 'mock_function'})() # pragma: no cover
F = Any # pragma: no cover
t.Any = Any # pragma: no cover
t.cast = lambda x, y: y # pragma: no cover

from typing import Any, Callable, TypeVar, cast # pragma: no cover
from functools import update_wrapper # pragma: no cover

class MockClass:# pragma: no cover
    def __init__(self, name):# pragma: no cover
        self.__name__ = name# pragma: no cover
# pragma: no cover
    def _check_setup_finished(self, name):# pragma: no cover
        print(f'Checking if setup finished for {name}') # pragma: no cover
f = MockClass('mock_function') # pragma: no cover
F = TypeVar('F', bound=Callable[..., Any]) # pragma: no cover
t = type('MockTyping', (object,), {'Any': Any, 'cast': cast}) # pragma: no cover

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
