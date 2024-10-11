from functools import wraps # pragma: no cover
from typing import Any, Callable, TypeVar # pragma: no cover

def f(self, *args, **kwargs): pass # pragma: no cover
t = TypeVar('t') # pragma: no cover
F = Callable[..., Any] # pragma: no cover
update_wrapper = wraps # pragma: no cover

from functools import wraps # pragma: no cover
from typing import Any, Callable, TypeVar # pragma: no cover

def f(self, *args, **kwargs): pass # pragma: no cover
t = type('Mock', (object,), {'Any': Any}) # pragma: no cover
F = Callable[..., Any] # pragma: no cover
update_wrapper = wraps # pragma: no cover

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
