import inspect # pragma: no cover
import functools # pragma: no cover
from types import MethodType # pragma: no cover
from collections.abc import Coroutine # pragma: no cover

func = MethodType(lambda x: x, object()) # pragma: no cover
inspect = type('MockInspect', (object,), {'ismethod': lambda x: isinstance(x, MethodType), 'iscoroutinefunction': lambda x: isinstance(x, Coroutine)})() # pragma: no cover
functools = type('MockFunctools', (object,), {'partial': type('MockPartial', (object,), {'func': lambda x: x})})() # pragma: no cover

import inspect # pragma: no cover
import functools # pragma: no cover
from types import MethodType # pragma: no cover
from collections.abc import Coroutine # pragma: no cover

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
