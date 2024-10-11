from functools import update_wrapper # pragma: no cover
import typing as t # pragma: no cover

class F:  # Mock class to hold methods for the wrapper function # pragma: no cover
    def _check_setup_finished(self, f_name):  # Mock method implementation # pragma: no cover
        print(f'Checking setup for: {f_name}') # pragma: no cover
 # pragma: no cover
def f(self, *args, **kwargs): return 100  # Mock function to replace f # pragma: no cover
 # pragma: no cover
instance = F()  # Create an instance of F # pragma: no cover
f_name = f.__name__  # Get the name of the function f # pragma: no cover
 # pragma: no cover
def wrapper_func(self, *args: t.Any, **kwargs: t.Any) -> t.Any:  # Definition of the wrapper function # pragma: no cover
    self._check_setup_finished(f_name)  # Call the mock method # pragma: no cover
    aux = f(self, *args, **kwargs)  # Call the wrapped function # pragma: no cover
    return aux  # Return the result instead of exiting # pragma: no cover
 # pragma: no cover
aux = t.cast(F, update_wrapper(wrapper_func, f))  # Update the wrapper function with metadata from f # pragma: no cover

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
