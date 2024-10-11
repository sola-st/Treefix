from functools import update_wrapper # pragma: no cover
import typing as t # pragma: no cover

class MockSelf:  # Mock class to represent 'self' in wrapper_func # pragma: no cover
    def _check_setup_finished(self, f_name):  # Mock method to simulate action # pragma: no cover
        print(f'{f_name} setup checked') # pragma: no cover
 # pragma: no cover
def f(self, *args, **kwargs):  # Mock function to replace f # pragma: no cover
    return 'Function executed' # pragma: no cover
 # pragma: no cover
instance = MockSelf()  # Create an instance of the mock class # pragma: no cover
f_name = f.__name__  # Get the name of the function f # pragma: no cover
 # pragma: no cover
def wrapper_func(self, *args: t.Any, **kwargs: t.Any) -> t.Any:  # Wrapper function # pragma: no cover
    self._check_setup_finished(f_name)  # uncovered # pragma: no cover
    aux = f(self, *args, **kwargs)  # uncovered # pragma: no cover
    return aux  # Return the execution result instead of exiting # pragma: no cover
 # pragma: no cover
wrapped_function = t.cast(MockSelf, update_wrapper(wrapper_func, f)) # pragma: no cover

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
