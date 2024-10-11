from functools import update_wrapper # pragma: no cover
from typing import Any, cast # pragma: no cover

from functools import update_wrapper # pragma: no cover
from typing import Any, cast # pragma: no cover

class MockSelf:# pragma: no cover
    def _check_setup_finished(self, name: str):# pragma: no cover
        print(f'Check setup finished for {name}') # pragma: no cover
f = lambda self, *args, **kwargs: 0 # pragma: no cover
f.__name__ = 'mock_function' # pragma: no cover
t = type('MockTyping', (object,), {'Any': Any, 'cast': cast}) # pragma: no cover
F = type('MockF', (object,), {})() # pragma: no cover
update_wrapper = lambda wrapper, wrapped, assigned=('__module__', '__name__', '__qualname__', '__annotations__'), updated=('__dict__',): wrapper# pragma: no cover

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
