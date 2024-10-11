import inspect # pragma: no cover
import functools # pragma: no cover

import inspect # pragma: no cover
import functools # pragma: no cover

func = lambda x: x # pragma: no cover
class MockPartial:# pragma: no cover
    def __init__(self, func):# pragma: no cover
        self.func = func# pragma: no cover
# pragma: no cover
functools.partial = MockPartial(func) # pragma: no cover
inspect.ismethod = lambda x: hasattr(x, '__func__') # pragma: no cover
inspect.iscoroutinefunction = lambda x: False # pragma: no cover

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
