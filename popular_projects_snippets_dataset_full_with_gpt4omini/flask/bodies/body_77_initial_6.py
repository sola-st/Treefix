import inspect # pragma: no cover
import functools # pragma: no cover

func = lambda: None # pragma: no cover
inspect = type('MockInspect', (object,), {'ismethod': staticmethod(lambda x: False), 'iscoroutinefunction': staticmethod(lambda x: False)})() # pragma: no cover
functools = type('MockFunctools', (object,), {'partial': type('MockPartial', (object,), {'func': func})})() # pragma: no cover

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
