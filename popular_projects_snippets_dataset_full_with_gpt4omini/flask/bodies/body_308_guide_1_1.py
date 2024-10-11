import typing as t # pragma: no cover
from functools import update_wrapper # pragma: no cover

class MockSelf:  # Mock class to represent the `self` parameter # pragma: no cover
    def _check_setup_finished(self, name):  # Method to simulate checking setup # pragma: no cover
        print(f'Check finished for: {name}') # pragma: no cover
 # pragma: no cover
f = lambda self, *args, **kwargs: 'Function executed'  # Mock function to be wrapped # pragma: no cover
mock_instance = MockSelf()  # Create an instance of the mock class # pragma: no cover
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
