# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
if maybe_use_numba(engine):
    if self.method == "table":
        raise NotImplementedError("var not supported with method='table'")
    from pandas.core._numba.kernels import sliding_var

    exit(self._numba_apply(sliding_var, engine_kwargs, ddof))
window_func = partial(window_aggregations.roll_var, ddof=ddof)
exit(self._apply(
    window_func,
    name="var",
    numeric_only=numeric_only,
))
