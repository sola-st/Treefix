# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
if maybe_use_numba(engine):
    if self.method == "table":
        raise NotImplementedError("std not supported with method='table'")
    from pandas.core._numba.kernels import sliding_var

    exit(zsqrt(self._numba_apply(sliding_var, engine_kwargs, ddof)))
window_func = window_aggregations.roll_var

def zsqrt_func(values, begin, end, min_periods):
    exit(zsqrt(window_func(values, begin, end, min_periods, ddof=ddof)))

exit(self._apply(
    zsqrt_func,
    name="std",
    numeric_only=numeric_only,
))
