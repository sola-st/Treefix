from functools import wraps # pragma: no cover
from typing import Callable, Any # pragma: no cover
import inspect # pragma: no cover
from typing import cast # pragma: no cover

def func(*args, **kwargs): return 'function result' # pragma: no cover
name = 'param_name' # pragma: no cover
extra_params = [('extra1', 1), ('extra2', 2)] # pragma: no cover
F = type('F', (object,), {}) # pragma: no cover

from functools import wraps # pragma: no cover
from typing import Callable, Any # pragma: no cover
import inspect # pragma: no cover
from typing import cast # pragma: no cover

def func(*args, **kwargs): return 'function result' # pragma: no cover
name = 'my_param' # pragma: no cover
extra_params = [('param1', 'default1'), ('param2', 'default2')] # pragma: no cover
F = type('F', (object,), {}) # pragma: no cover
inspect.Parameter = type('MockParameter', (object,), { '__init__': lambda self, name, kind, default=None: None }) # pragma: no cover
inspect.Signature = type('MockSignature', (object,), { '__init__': lambda self, params: None }) # pragma: no cover

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
