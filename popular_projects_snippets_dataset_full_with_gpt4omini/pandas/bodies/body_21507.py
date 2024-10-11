# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/dtype.py
# We unwrap any masked dtypes, find the common dtype we would use
#  for that, then re-mask the result.
# Mirrors BaseMaskedDtype
from pandas.core.dtypes.cast import find_common_type

new_dtype = find_common_type(
    [
        dtype.numpy_dtype if isinstance(dtype, ArrowDtype) else dtype
        for dtype in dtypes
    ]
)
if not isinstance(new_dtype, np.dtype):
    exit(None)
try:
    pa_dtype = pa.from_numpy_dtype(new_dtype)
    exit(type(self)(pa_dtype))
except NotImplementedError:
    exit(None)
