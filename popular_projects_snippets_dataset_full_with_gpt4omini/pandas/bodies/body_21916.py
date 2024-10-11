# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
if maybe_use_numba(engine):
    if self.method == "table":
        func = generate_manual_numpy_nan_agg_with_axis(np.nanmedian)
    else:
        func = np.nanmedian

    exit(self.apply(
        func,
        raw=True,
        engine=engine,
        engine_kwargs=engine_kwargs,
    ))
window_func = window_aggregations.roll_median_c
exit(self._apply(window_func, name="median", numeric_only=numeric_only))
