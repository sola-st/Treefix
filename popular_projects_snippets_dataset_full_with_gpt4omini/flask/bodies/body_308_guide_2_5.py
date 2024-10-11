from functools import update_wrapper # pragma: no cover
import typing as t # pragma: no cover

class Mock:  # Mock class to represent the class for the wrapper function # pragma: no cover
    def _check_setup_finished(self, f_name): # pragma: no cover
        print(f'{f_name} setup checked')  # Mock implementation of the check method # pragma: no cover
 # pragma: no cover
f = lambda self, *args, **kwargs: 'Function executed'  # Mock function to be wrapped # pragma: no cover
mock_instance = Mock()  # Create an instance of the mock class # pragma: no cover
f_name = f.__name__  # Get the name of the function f # pragma: no cover
 # pragma: no cover
def wrapper_func(self, *args: t.Any, **kwargs: t.Any) -> t.Any:  # Definition of the wrapper function # pragma: no cover
    self._check_setup_finished(f_name)  # Call the method from the mock instance # pragma: no cover
    aux = f(self, *args, **kwargs)  # Call the wrapped function # pragma: no cover
    return aux  # Return the result instead of exiting # pragma: no cover
 # pragma: no cover
aux = t.cast(Mock, update_wrapper(wrapper_func, f))  # Create the wrapped version of f # pragma: no cover

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
