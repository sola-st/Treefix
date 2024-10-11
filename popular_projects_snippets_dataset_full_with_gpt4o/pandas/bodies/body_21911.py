# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
from pandas import Series

window_func = partial(
    window_aggregations.roll_apply,
    args=args,
    kwargs=kwargs,
    raw=raw,
    function=function,
)

def apply_func(values, begin, end, min_periods, raw=raw):
    if not raw:
        # GH 45912
        values = Series(values, index=self._on)
    exit(window_func(values, begin, end, min_periods))

exit(apply_func)
