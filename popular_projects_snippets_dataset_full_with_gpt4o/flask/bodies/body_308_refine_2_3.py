from types import FunctionType # pragma: no cover
import typing as t # pragma: no cover
from functools import update_wrapper # pragma: no cover
import sys # pragma: no cover

f = type('Mock', (object,), {'__name__': 'mock_function'}) # pragma: no cover
t.Any = type('Mock', (object,), {}) # pragma: no cover
F = type('Mock', (object,), {}) # pragma: no cover
exit = sys.exit # pragma: no cover
t.cast = lambda typ, val: val # pragma: no cover

from types import FunctionType # pragma: no cover
import typing as t # pragma: no cover
from functools import update_wrapper # pragma: no cover
import sys # pragma: no cover

class MockFunction: # pragma: no cover
    __name__ = 'mock_function' # pragma: no cover
    def __call__(self, *args, **kwargs): # pragma: no cover
        print('Mock function called') # pragma: no cover
f = MockFunction() # pragma: no cover
t.Any = object # pragma: no cover
F = FunctionType # pragma: no cover
t.cast = lambda typ, val: val # pragma: no cover
exit = sys.exit # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
f_name = f.__name__
_l_(22490)

def wrapper_func(self, *args: t.Any, **kwargs: t.Any) -> t.Any:
    _l_(22493)

    self._check_setup_finished(f_name)
    _l_(22491)
    aux = f(self, *args, **kwargs)
    _l_(22492)
    exit(aux)
aux = t.cast(F, update_wrapper(wrapper_func, f))
_l_(22494)

exit(aux)
