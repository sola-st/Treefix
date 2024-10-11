import inspect # pragma: no cover
import functools # pragma: no cover

func = functools.partial(lambda x: x + 1, 5) # pragma: no cover

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
