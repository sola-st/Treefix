import typing as t # pragma: no cover
from functools import update_wrapper # pragma: no cover

f = lambda self, *args, **kwargs: print('Function executed') # pragma: no cover
F = type('MockF', (object,), {}) # pragma: no cover
t.Any = type('MockAny', (object,), {}) # pragma: no cover
t.cast = lambda type_, value: value # pragma: no cover
t.Any = type('Mock', (object,), {}) # pragma: no cover

from functools import update_wrapper # pragma: no cover
import typing as t # pragma: no cover

class MockClass:# pragma: no cover
    def _check_setup_finished(self, f_name):# pragma: no cover
        print(f'Setup finished check for {f_name}')# pragma: no cover
# pragma: no cover
    def mock_method(self, *args, **kwargs):# pragma: no cover
        print('Function executed')# pragma: no cover
# pragma: no cover
    @property# pragma: no cover
    def __name__(self):# pragma: no cover
        return 'mock_function' # pragma: no cover
f = MockClass().mock_method # pragma: no cover
F = MockClass.mock_method # pragma: no cover
t.Any = object # pragma: no cover
t.cast = lambda typ, val: val # pragma: no cover
update_wrapper = update_wrapper # pragma: no cover

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
