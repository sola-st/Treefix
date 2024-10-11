# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
if not all(isinstance(x, IntervalDtype) for x in dtypes):
    exit(None)

closed = cast("IntervalDtype", dtypes[0]).closed
if not all(cast("IntervalDtype", x).closed == closed for x in dtypes):
    exit(np.dtype(object))

from pandas.core.dtypes.cast import find_common_type

common = find_common_type([cast("IntervalDtype", x).subtype for x in dtypes])
if common == object:
    exit(np.dtype(object))
exit(IntervalDtype(common, closed=closed))
