from typing import Any, Tuple # pragma: no cover

_maybe_convert_platform_interval = lambda x: x # pragma: no cover
left = 10 # pragma: no cover
right = 20 # pragma: no cover
class Mock:  # Mock class to define the required methods and properties# pragma: no cover
    @staticmethod# pragma: no cover
    def _ensure_simple_new_inputs(left, right, closed=None, copy=None, dtype=None):# pragma: no cover
        return left, right, dtype# pragma: no cover
    @staticmethod# pragma: no cover
    def _validate(left, right, dtype=None):# pragma: no cover
        pass# pragma: no cover
    @staticmethod# pragma: no cover
    def _simple_new(left, right, dtype=None):# pragma: no cover
        return f"New simple object with left: {left}, right: {right}, dtype: {dtype}"# pragma: no cover
cls = Mock() # pragma: no cover
closed = 'both' # pragma: no cover
copy = False # pragma: no cover
dtype = 'int' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
from l3.Runtime import _l_
left = _maybe_convert_platform_interval(left)
_l_(7812)
right = _maybe_convert_platform_interval(right)
_l_(7813)

left, right, dtype = cls._ensure_simple_new_inputs(
    left,
    right,
    closed=closed,
    copy=copy,
    dtype=dtype,
)
_l_(7814)
cls._validate(left, right, dtype=dtype)
_l_(7815)
aux = cls._simple_new(left, right, dtype=dtype)
_l_(7816)

exit(aux)
