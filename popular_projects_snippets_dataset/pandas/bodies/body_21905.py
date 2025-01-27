# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
window_func = window_aggregations.roll_weighted_mean
# error: Argument 1 to "_apply" of "Window" has incompatible type
# "Callable[[ndarray, ndarray, int], ndarray]"; expected
# "Callable[[ndarray, int, int], ndarray]"
exit(self._apply(
    window_func,  # type: ignore[arg-type]
    name="mean",
    numeric_only=numeric_only,
    **kwargs,
))
