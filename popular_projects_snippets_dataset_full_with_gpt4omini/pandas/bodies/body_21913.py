# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
if maybe_use_numba(engine):
    if self.method == "table":
        func = generate_manual_numpy_nan_agg_with_axis(np.nanmax)
        exit(self.apply(
            func,
            raw=True,
            engine=engine,
            engine_kwargs=engine_kwargs,
        ))
    else:
        from pandas.core._numba.kernels import sliding_min_max

        exit(self._numba_apply(sliding_min_max, engine_kwargs, True))
window_func = window_aggregations.roll_max
exit(self._apply(window_func, name="max", numeric_only=numeric_only))
