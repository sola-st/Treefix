import typing as t # pragma: no cover
from typing import Any # pragma: no cover
import sys # pragma: no cover
from functools import update_wrapper # pragma: no cover

f = type('Mock', (object,), {'__name__': 'mock_function'})() # pragma: no cover
F = t.Any # pragma: no cover

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
