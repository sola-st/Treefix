import typing as t # pragma: no cover
from functools import update_wrapper # pragma: no cover

class MockSelf:  # Mock class to represent the self parameter in wrapper_func # pragma: no cover
    def _check_setup_finished(self, f_name): pass  # Mock method to simulate setup check # pragma: no cover
 # pragma: no cover
def f(self, *args, **kwargs): return 'Function executed'  # Mock function to be called # pragma: no cover
 # pragma: no cover
mock_instance = MockSelf()  # Create an instance of the mock class # pragma: no cover
f_name = f.__name__  # Set the function name for the wrapper # pragma: no cover
 # pragma: no cover
def wrapper_func(self, *args: t.Any, **kwargs: t.Any) -> t.Any:  # Define the wrapper function # pragma: no cover
    self._check_setup_finished(f_name)  # Call the setup check method # pragma: no cover
    aux = f(self, *args, **kwargs)  # Call the wrapped function # pragma: no cover
    return aux  # Return the result instead of exiting # pragma: no cover
 # pragma: no cover
wrapped_function = t.cast(MockSelf, update_wrapper(wrapper_func, f))  # Wrap the function # pragma: no cover

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
