import inspect # pragma: no cover
import functools # pragma: no cover

def sample_method(self): pass # pragma: no cover
class Mock:  # pragma: no cover
    method = sample_method # pragma: no cover
func = Mock.method # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
while inspect.ismethod(func):
    _l_(6921)

    func = func.__func__
    _l_(6920)

while isinstance(func, functools.partial):
    _l_(6923)

    func = func.func
    _l_(6922)
aux = inspect.iscoroutinefunction(func)
_l_(6924)

exit(aux)
