from functools import wraps # pragma: no cover
from typing import Callable, Any # pragma: no cover
import inspect # pragma: no cover
from typing import cast # pragma: no cover

def func(*args, **kwargs): return args, kwargs # pragma: no cover
name = 'my_param' # pragma: no cover
extra_params = [('param1', 'default1'), ('param2', 'default2')] # pragma: no cover
class F: pass # pragma: no cover
inspect.Parameter = type('MockParameter', (object,), { 'POSITIONAL_OR_KEYWORD': 0 }) # pragma: no cover
inspect.Signature = type('MockSignature', (object,), {}) # pragma: no cover
func.__signature__ = inspect.Signature() # pragma: no cover

from functools import wraps # pragma: no cover
from typing import Callable, Any # pragma: no cover
import inspect # pragma: no cover
from typing import cast # pragma: no cover

def func(*args, **kwargs): return args, kwargs # pragma: no cover
name = 'my_param' # pragma: no cover
extra_params = [('param1', 'default1'), ('param2', 'default2')] # pragma: no cover
class F: pass # pragma: no cover
class MockParameter:# pragma: no cover
    def __init__(self, name, kind, default=None):# pragma: no cover
        self.name = name# pragma: no cover
        self.kind = kind# pragma: no cover
        self.default = default# pragma: no cover
 # pragma: no cover
inspect.Parameter = MockParameter # pragma: no cover
class MockSignature:# pragma: no cover
    def __init__(self, parameters):# pragma: no cover
        self.parameters = parameters# pragma: no cover
 # pragma: no cover
inspect.Signature = MockSignature # pragma: no cover
func.__signature__ = inspect.Signature([]) # pragma: no cover

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
