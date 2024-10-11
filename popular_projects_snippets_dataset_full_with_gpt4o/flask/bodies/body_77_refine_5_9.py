import inspect # pragma: no cover
import functools # pragma: no cover

func = type('Mock', (object,), {'__func__': None, 'func': None})() # pragma: no cover
inspect.ismethod = lambda x: hasattr(x, '__func__') # pragma: no cover
inspect.iscoroutinefunction = lambda x: False # pragma: no cover
functools.partial = type('MockPartial', (object,), {'func': None})() # pragma: no cover

import inspect # pragma: no cover
import functools # pragma: no cover

class MockFunc:# pragma: no cover
    __func__ = type('func_attr', (object,), {})()# pragma: no cover
    func = type('func_attr', (object,), {})() # pragma: no cover
func = MockFunc() # pragma: no cover
inspect.ismethod = lambda x: hasattr(x, '__func__') # pragma: no cover
inspect.iscoroutinefunction = lambda x: False # pragma: no cover
class MockPartial(functools.partial):# pragma: no cover
    func = type('func_attr', (object,), {})() # pragma: no cover
functools.partial = MockPartial # pragma: no cover

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
