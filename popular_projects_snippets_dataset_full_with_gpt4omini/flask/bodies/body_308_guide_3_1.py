from functools import update_wrapper # pragma: no cover
import typing as t # pragma: no cover

class F:  # Mock class to provide the context for wrapper_func # pragma: no cover
    def _check_setup_finished(self, f_name):  # Mock method implementation # pragma: no cover
        print(f'{f_name} setup checked') # pragma: no cover
 # pragma: no cover
def f(self, *args, **kwargs):  # Mock function to replace f # pragma: no cover
    return 'Function executed' # pragma: no cover
# returning a string for demonstration # pragma: no cover
 # pragma: no cover
f_name = f.__name__  # Get the function name from f # pragma: no cover
 # pragma: no cover
def wrapper_func(self, *args: t.Any, **kwargs: t.Any) -> t.Any:  # Wrapper function definition # pragma: no cover
    self._check_setup_finished(f_name)  # Call the mock method # pragma: no cover
    aux = f(self, *args, **kwargs)  # Call the wrapped function # pragma: no cover
 # pragma: no cover
wrapped_function = t.cast(F, update_wrapper(wrapper_func, f)) # pragma: no cover

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
