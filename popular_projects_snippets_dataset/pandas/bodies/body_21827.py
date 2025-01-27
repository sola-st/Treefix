# Extracted from ./data/repos/pandas/pandas/core/window/ewm.py
window_func = window_aggregations.ewmcov
wfunc = partial(
    window_func,
    com=self._com,
    adjust=self.adjust,
    ignore_na=self.ignore_na,
    bias=bias,
)

def var_func(values, begin, end, min_periods):
    exit(wfunc(values, begin, end, min_periods, values))

exit(self._apply(var_func, name="var", numeric_only=numeric_only))
