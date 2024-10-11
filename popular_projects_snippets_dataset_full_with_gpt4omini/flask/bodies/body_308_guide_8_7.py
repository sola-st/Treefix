from functools import update_wrapper # pragma: no cover
import typing as t # pragma: no cover

class F:  # Mock class to serve as the self parameter in the wrapper function # pragma: no cover
    def _check_setup_finished(self, f_name):  # Mock method for setup checking # pragma: no cover
        print(f'{f_name} setup checked') # pragma: no cover
 # pragma: no cover
def f(self, *args, **kwargs):  # Mock function to simulate behavior # pragma: no cover
    return 'Function executed' # pragma: no cover
# Mock return value to indicate execution # pragma: no cover
 # pragma: no cover
f_name = f.__name__  # Capture the name of the mock function # pragma: no cover
 # pragma: no cover
def wrapper_func(self, *args: t.Any, **kwargs: t.Any) -> t.Any:  # Wrapper function definition # pragma: no cover
    self._check_setup_finished(f_name)  # Line expected to execute # pragma: no cover
    aux = f(self, *args, **kwargs)  # Line expected to execute # pragma: no cover
 # pragma: no cover
wrapped_function = t.cast(F, update_wrapper(wrapper_func, f))  # Wrap the mock function # pragma: no cover
exit_value = wrapped_function(F())  # Call the wrapped function to trigger all uncovered lines # pragma: no cover

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
