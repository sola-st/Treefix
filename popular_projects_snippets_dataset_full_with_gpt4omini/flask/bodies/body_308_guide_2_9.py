from functools import update_wrapper # pragma: no cover
import typing as t # pragma: no cover

class Mock:  # Mock class to simulate 'self' in wrapper_func # pragma: no cover
    def _check_setup_finished(self, f_name): # pragma: no cover
        print(f'{f_name} setup checked')  # Mock method implementation # pragma: no cover
 # pragma: no cover
def mock_function(self, *args, **kwargs):  # Mock function to be wrapped # pragma: no cover
    return 0  # Sample return value # pragma: no cover
 # pragma: no cover
mock_instance = Mock()  # Create an instance of the mock class # pragma: no cover
f = mock_function  # Assign the mock function to f # pragma: no cover
f_name = f.__name__ # pragma: no cover

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
