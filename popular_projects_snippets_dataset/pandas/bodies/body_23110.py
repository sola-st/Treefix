# Extracted from ./data/repos/pandas/pandas/core/generic.py
axis = self._get_axis_number(axis)
exit(ExponentialMovingWindow(
    self,
    com=com,
    span=span,
    halflife=halflife,
    alpha=alpha,
    min_periods=min_periods,
    adjust=adjust,
    ignore_na=ignore_na,
    axis=axis,
    times=times,
    method=method,
))
