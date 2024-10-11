import inspect # pragma: no cover
import functools # pragma: no cover

func = type('MockFunc', (object,), {'__func__': None, 'func': None})() # pragma: no cover
inspect.ismethod = lambda func: hasattr(func, '__func__') # pragma: no cover
inspect.iscoroutinefunction = lambda func: False # pragma: no cover
functools.partial = type('MockPartial', (object,), {'func': None})() # pragma: no cover

import inspect # pragma: no cover
import functools # pragma: no cover

class MockFunc: pass # pragma: no cover
func = MockFunc() # pragma: no cover
func.__func__ = None # pragma: no cover
func.func = None # pragma: no cover
class MockPartial(functools.partial): pass # pragma: no cover
inspect.ismethod = lambda f: hasattr(f, '__func__') # pragma: no cover
inspect.iscoroutinefunction = lambda f: False # pragma: no cover

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
