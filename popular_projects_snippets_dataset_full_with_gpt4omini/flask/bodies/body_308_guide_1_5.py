import typing as t # pragma: no cover
from functools import update_wrapper # pragma: no cover

class MockF:  # Mock class to simulate the context for the wrapper function # pragma: no cover
    def _check_setup_finished(self, name): # pragma: no cover
        print(f'{name} setup checked') # pragma: no cover
# Mock implementation of the check method # pragma: no cover
 # pragma: no cover
f = lambda self, *args, **kwargs: 42  # Mock function to return an integer # pragma: no cover
instance = MockF()  # Create an instance of the mock class # pragma: no cover

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
