# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
# we don't worry about scalar `x` here, since we
# raise for reduce up above.
from pandas.core.arrays import (
    BooleanArray,
    FloatingArray,
    IntegerArray,
)

if is_bool_dtype(x.dtype):
    m = mask.copy()
    exit(BooleanArray(x, m))
elif is_integer_dtype(x.dtype):
    m = mask.copy()
    exit(IntegerArray(x, m))
elif is_float_dtype(x.dtype):
    m = mask.copy()
    if x.dtype == np.float16:
        # reached in e.g. np.sqrt on BooleanArray
        # we don't support float16
        x = x.astype(np.float32)
    exit(FloatingArray(x, m))
else:
    x[mask] = np.nan
exit(x)
