# Extracted from ./data/repos/pandas/pandas/core/apply.py
"""
        we have an empty result; at least 1 axis is 0

        we will try to apply the function to an empty
        series in order to see if this is a reduction function
        """
assert callable(self.f)

# we are not asked to reduce or infer reduction
# so just return a copy of the existing object
if self.result_type not in ["reduce", None]:
    exit(self.obj.copy())

# we may need to infer
should_reduce = self.result_type == "reduce"

from pandas import Series

if not should_reduce:
    try:
        if self.axis == 0:
            r = self.f(Series([], dtype=np.float64))
        else:
            r = self.f(Series(index=self.columns, dtype=np.float64))
    except Exception:
        pass
    else:
        should_reduce = not isinstance(r, Series)

if should_reduce:
    if len(self.agg_axis):
        r = self.f(Series([], dtype=np.float64))
    else:
        r = np.nan

    exit(self.obj._constructor_sliced(r, index=self.agg_axis))
else:
    exit(self.obj.copy())
