from functools import wraps # pragma: no cover
from typing import Callable, Any, List, Tuple, TypeVar, cast # pragma: no cover
import inspect # pragma: no cover
import sys # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/util/_decorators.py
from l3.Runtime import _l_
@wraps(func)
def wrapper(*args, **kwargs) -> Callable[..., Any]:
    _l_(21459)

    aux = func(*args, **kwargs)
    _l_(21458)
    exit(aux)

kind = inspect.Parameter.POSITIONAL_OR_KEYWORD
_l_(21460)
params = [
    inspect.Parameter("self", kind),
    inspect.Parameter(name, kind, default=None),
    inspect.Parameter("index", kind, default=None),
    inspect.Parameter("columns", kind, default=None),
    inspect.Parameter("axis", kind, default=None),
]
_l_(21461)

for pname, default in extra_params:
    _l_(21463)

    params.append(inspect.Parameter(pname, kind, default=default))
    _l_(21462)

sig = inspect.Signature(params)
_l_(21464)

# https://github.com/python/typing/issues/598
# error: "F" has no attribute "__signature__"
func.__signature__ = sig  # type: ignore[attr-defined]
_l_(21465)  # type: ignore[attr-defined]
aux = cast(F, wrapper)
_l_(21466)
exit(aux)
