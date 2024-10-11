_maybe_convert_platform_interval = lambda x: x # pragma: no cover
left = 0 # pragma: no cover
right = 10 # pragma: no cover
closed = 'both' # pragma: no cover
copy = False # pragma: no cover
dtype = int # pragma: no cover
cls = type('Mock', (object,), {'_ensure_simple_new_inputs': staticmethod(lambda left, right, closed, copy, dtype: (left, right, dtype)), '_validate': staticmethod(lambda left, right, dtype: None), '_simple_new': staticmethod(lambda left, right, dtype: (left, right, dtype))}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
from l3.Runtime import _l_
left = _maybe_convert_platform_interval(left)
_l_(20233)
right = _maybe_convert_platform_interval(right)
_l_(20234)

left, right, dtype = cls._ensure_simple_new_inputs(
    left,
    right,
    closed=closed,
    copy=copy,
    dtype=dtype,
)
_l_(20235)
cls._validate(left, right, dtype=dtype)
_l_(20236)
aux = cls._simple_new(left, right, dtype=dtype)
_l_(20237)

exit(aux)
