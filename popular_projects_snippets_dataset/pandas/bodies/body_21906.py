# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
window_func = partial(window_aggregations.roll_weighted_var, ddof=ddof)
kwargs.pop("name", None)
exit(self._apply(window_func, name="var", numeric_only=numeric_only, **kwargs))
