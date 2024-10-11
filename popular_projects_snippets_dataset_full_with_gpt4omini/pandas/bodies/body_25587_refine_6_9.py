from functools import wraps # pragma: no cover
from typing import Callable, Any, cast # pragma: no cover
import inspect # pragma: no cover

func = lambda x: x * 2 # pragma: no cover
name = 'column_name' # pragma: no cover
extra_params = [('param1', 1), ('param2', 2)] # pragma: no cover
F = type('F', (object,), {}) # pragma: no cover

from functools import wraps # pragma: no cover
from typing import Callable, Any # pragma: no cover
import inspect # pragma: no cover

def func(*args, **kwargs): return args, kwargs # pragma: no cover
name = 'example_param' # pragma: no cover
extra_params = [('extra1', 1), ('extra2', 2)] # pragma: no cover
class F: pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/util/_decorators.py
from l3.Runtime import _l_
@wraps(func)
def wrapper(*args, **kwargs) -> Callable[..., Any]:
    _l_(10440)

    aux = func(*args, **kwargs)
    _l_(10439)
    exit(aux)

kind = inspect.Parameter.POSITIONAL_OR_KEYWORD
_l_(10441)
params = [
    inspect.Parameter("self", kind),
    inspect.Parameter(name, kind, default=None),
    inspect.Parameter("index", kind, default=None),
    inspect.Parameter("columns", kind, default=None),
    inspect.Parameter("axis", kind, default=None),
]
_l_(10442)

for pname, default in extra_params:
    _l_(10444)

    params.append(inspect.Parameter(pname, kind, default=default))
    _l_(10443)

sig = inspect.Signature(params)
_l_(10445)

# https://github.com/python/typing/issues/598
# error: "F" has no attribute "__signature__"
func.__signature__ = sig  # type: ignore[attr-defined]
_l_(10446)  # type: ignore[attr-defined]
aux = cast(F, wrapper)
_l_(10447)
exit(aux)
