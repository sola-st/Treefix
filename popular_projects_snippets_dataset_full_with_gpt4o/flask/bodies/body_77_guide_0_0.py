import inspect # pragma: no cover
import functools # pragma: no cover

def mock_func(): pass # pragma: no cover
mock_partial = functools.partial(mock_func) # pragma: no cover
func = mock_partial # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
while inspect.ismethod(func):
    _l_(22748)

    func = func.__func__
    _l_(22747)

while isinstance(func, functools.partial):
    _l_(22750)

    func = func.func
    _l_(22749)
aux = inspect.iscoroutinefunction(func)
_l_(22751)

exit(aux)
