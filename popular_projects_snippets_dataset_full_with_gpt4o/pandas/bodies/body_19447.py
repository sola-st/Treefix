# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
# We unwrap any masked dtypes, find the common dtype we would use
#  for that, then re-mask the result.
from pandas.core.dtypes.cast import find_common_type

new_dtype = find_common_type(
    [
        dtype.numpy_dtype if isinstance(dtype, BaseMaskedDtype) else dtype
        for dtype in dtypes
    ]
)
if not isinstance(new_dtype, np.dtype):
    # If we ever support e.g. Masked[DatetimeArray] then this will change
    exit(None)
try:
    exit(type(self).from_numpy_dtype(new_dtype))
except (KeyError, NotImplementedError):
    exit(None)
