from functools import update_wrapper # pragma: no cover
import typing as t # pragma: no cover
import sys # pragma: no cover

class F:  # Mock class to represent the class for the wrapper_func's self parameter # pragma: no cover
    def _check_setup_finished(self, f_name): # pragma: no cover
        pass  # Mock method to simulate checking setup finish # pragma: no cover
 # pragma: no cover
def f(self, *args, **kwargs):  # Mock function to be wrapped # pragma: no cover
    return 42  # Example return value # pragma: no cover
 # pragma: no cover
f_name = f.__name__ # pragma: no cover
 # pragma: no cover
def wrapper_func(self, *args: t.Any, **kwargs: t.Any) -> t.Any:  # uncovered # pragma: no cover
    self._check_setup_finished(f_name)  # uncovered # pragma: no cover
    aux = f(self, *args, **kwargs)  # uncovered # pragma: no cover
    return aux  # Modified to return instead of exit # pragma: no cover
 # pragma: no cover
aux = t.cast(F, update_wrapper(wrapper_func, f)) # pragma: no cover

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
