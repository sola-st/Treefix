import typing as t # pragma: no cover
from functools import update_wrapper # pragma: no cover

class Mock: pass # pragma: no cover
mock_instance = Mock() # pragma: no cover
setattr(mock_instance, '_check_setup_finished', lambda f_name: None) # pragma: no cover
f = lambda self, *args, **kwargs: 'Function executed' # pragma: no cover
F = type('F', (object,), {}) # pragma: no cover

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
