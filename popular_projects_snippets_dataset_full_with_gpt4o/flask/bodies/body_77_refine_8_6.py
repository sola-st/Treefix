import inspect # pragma: no cover
import functools # pragma: no cover

func = type('MockFunc', (object,), {'__func__': lambda self: None, 'func': lambda self: None})() # pragma: no cover
inspect.ismethod = lambda x: True # pragma: no cover
functools.partial = type('MockPartial', (object,), {'func': lambda self: None}) # pragma: no cover
inspect.iscoroutinefunction = lambda x: False # pragma: no cover

import inspect # pragma: no cover
import functools # pragma: no cover

func = type('MockFunc', (object,), {'__func__': (lambda: None)})() # pragma: no cover
inspect.ismethod = lambda x: hasattr(x, '__func__') # pragma: no cover
functools.partial = type('MockPartial', (object,), {'func': (lambda: None)}) # pragma: no cover
inspect.iscoroutinefunction = lambda x: False # pragma: no cover

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
